from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from src.toolfuzz.correctness.prompt_generation.llm_responses import CorrectnessResponse, RelevanceResponse
from src.toolfuzz.correctness.prompt_generation.prompts import correctness_prompt, tool_output_correctness, \
    relevance_prompt
from src.toolfuzz.dataclasses import Bucket
from src.toolfuzz.logging_mixin import LoggingMixin


class CorrectnessOracle(LoggingMixin):
    def __init__(self, model='gpt-4o'):
        super().__init__()
        model = ChatOpenAI(model=model, temperature=0)
        parser = JsonOutputParser(pydantic_object=CorrectnessResponse)
        prompt = PromptTemplate(
            template=correctness_prompt,
            input_variables=['tool_output', 'agent_output', 'expected'],
            partial_variables={"format_instructions": parser.get_format_instructions()})
        self.chain = prompt | model | parser

        parser = JsonOutputParser(pydantic_object=CorrectnessResponse)
        prompt = PromptTemplate(
            template=tool_output_correctness,
            input_variables=['tool_output', 'expected'],
            partial_variables={"format_instructions": parser.get_format_instructions()})
        self.tool_out_chain = prompt | model | parser

        parser = JsonOutputParser(pydantic_object=RelevanceResponse)
        is_out_relevant = PromptTemplate(
            template=relevance_prompt,
            input_variables=['question', 'tool_output', 'agent_out', 'llm_expect'],
            partial_variables={"format_instructions": parser.get_format_instructions()}
        )
        self.relevance_chain = is_out_relevant | model | parser

    def is_tool_output_correct(self, tool_output, expected, attempt=3):
        if attempt == 0:
            return False, 'Failed to parse judge LLM response'
        try:
            response = self.tool_out_chain.invoke({'tool_output': tool_output, 'expected': expected})
            return response['is_correct'], response['reason']
        except OutputParserException as e:
            self.log_error(f"Error during evaluation of the result {e}")
            return self.is_tool_output_correct(tool_output, expected, attempt - 1)
        except KeyError as e:
            self.log_error(f"Error during evaluation of the result {e}")
            return self.is_tool_output_correct(tool_output, expected, attempt - 1)

    def agent_out_correctness(self, agent_answer, tool_message, expected, attempt=3):
        if attempt == 0:
            return False, 'Failed to parse judge LLM response'
        try:
            model_response = self.chain.invoke(
                {'agent_output': agent_answer, 'tool_output': tool_message, 'expected': expected})
            return model_response['correctness_degree'], model_response['reason']
        except OutputParserException:
            self.log_error("Failed to parse judge LLM response")
            return self.is_agent_output_relevant(agent_answer, tool_message, expected, attempt - 1)
        except KeyError as e:
            self.log_error(f"Error during evaluation of the result {e}")
            return self.is_agent_output_relevant(agent_answer, tool_message, expected, attempt - 1)

    def is_agent_output_relevant(self, agent_out, prompt, tool_output, llm_expect, attempt=3):
        if attempt == 0:
            return False, 'Failed to parse judge LLM response'
        try:
            model_response = self.relevance_chain.invoke(
                {'question': prompt, 'tool_output': tool_output, 'agent_out': agent_out, 'llm_expect': llm_expect})
            return model_response['is_relevant'], model_response['reason']
        except OutputParserException:
            self.log_error("Failed to parse judge LLM response")
            return self.is_agent_output_relevant(agent_out, prompt, tool_output, llm_expect, attempt - 1)
        except KeyError as e:
            self.log_error(f"Error during evaluation of the result {e}")
            return self.is_agent_output_relevant(agent_out, prompt, tool_output, llm_expect, attempt - 1)

    @staticmethod
    def evaluate_tool_output(agent_outs):
        # Group and check
        buckets = {}
        for agent_res, prompt in agent_outs:
            tool_out = agent_res.tool_output
            assert isinstance(tool_out, list) or isinstance(tool_out, str)
            if isinstance(tool_out, list):
                if len(tool_out) == 0:
                    add_to_bucket(buckets, '', prompt)
                for out in tool_out:
                    add_to_bucket(buckets, out, prompt)
            elif isinstance(tool_out, str):
                add_to_bucket(buckets, tool_out, prompt)
        # So no special thing if all the outs are the same:
        transformed_buckets = [Bucket(bucket_items=prompts, bucket_value=output) for output, prompts in
                               buckets.items()]
        for bucket in buckets:
            if len(buckets[bucket]) == len(agent_outs):
                return False, transformed_buckets
        return True, transformed_buckets

    @staticmethod
    def evaluate_tool_arguments(outs):
        buckets = {}
        for agent_out, prompt in outs:
            args = agent_out.tool_args
            add_to_bucket(buckets, args, prompt)

        transformed_buckets = [Bucket(bucket_items=prompts, bucket_value=str(args)) for args, prompts in
                               buckets.items()]

        for bucket in buckets:
            if len(buckets[bucket]) == len(outs):
                return False, transformed_buckets
        return True, transformed_buckets


def add_to_bucket(buckets, key, value):
    key = str(key)  # Some tools have structured output i.e. list/dict
    if key in buckets:
        buckets[key].append(value)
    elif key not in buckets:
        buckets[key] = [value]


def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
