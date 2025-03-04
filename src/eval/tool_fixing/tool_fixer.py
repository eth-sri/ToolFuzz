import json
import random
from typing import List

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

from src.eval.toolfuzz.loaders.langchain_tool_loaders import ShellToolLoader
from src.eval.toolfuzz.utils.setup import init_model
from src.toolfuzz.dataclasses import PromptSetTestResults, TestResult
from src.toolfuzz.tools.info_extractors.langchain_tool_wrapper import LangchainToolWrapper

IMPROVE_DESCRIPTION_EXAMPLES_TEMPLATE = """
You are an AI Agent Tool developer can you make the description of a tool more precise and clear. The problem is that the LLM sometimes doesn't translate the queries correctly.
This comes from the fact that the tool description doesn't explain what exactly is allowed and how to use the tool correctly.
The current description of the tool is: {tool_description}

Here are some failing examples of the tool in action:
{bad_examples}

Given the bad examples please identify the main issues on those examples and what is the cause of that issue.
How can these issues be avoided by validation i.e. with this tool or external resources or it's just a user mistake? List the main issues and how to avoid them.

Now that the issues and how to avoid them are clear. Please create tool description that addresses these issues. The description is a manual on how to use the tool correctly and what is allowed and what is not.
It should explain how to avoid the issues that were found in the examples. Add that the tool can be invoked multiple times for better validation of the file system state.

Also give few examples if you think they are applicable.

Please provide description which reflects these issues. The new description shouldn't be longer than 100 words.

{format_instructions}
"""

IMPROVE_DESCRIPTION_TEMPLATE = """
You are an AI Agent Tool developer can you make the description of a tool more precise and clear. The problem is that the LLM sometimes doesn't translate the queries correctly.
This comes from the fact that the tool description doesn't explain what exactly is allowed and how to use the tool correctly.
The current description of the tool is: {tool_description}

The description has to be a manual on how to use the tool correctly and what is allowed and what is not.
Please provide just the new description of the tool.
{format_instructions}
"""

IMPROVE_DESCRIPTION_SRC_TEMPLATE = """
You are an AI Agent Tool developer can you make the description of a tool more precise and clear. The problem is that the LLM sometimes doesn't translate the queries correctly.
This comes from the fact that the tool description doesn't explain what exactly is allowed and how to use the tool correctly.
The current description of the tool is: {tool_description}
The source code of the tool is: {tool_source_code}

The description has to be a manual on how to use the tool correctly and what is allowed and what is not.
Please provide just the new description of the tool.
{format_instructions}
"""

IMPROVE_FIELD_DESCRIPTION_EXAMPLES = """
You are an AI Agent Tool developer can you make the description of a tool more precise and clear.
The name of the field is: {field_name}
The description of the field is: {field_description}

Please provide just the new description of the field. The new description shouldn't be longer than 30 words and here are some examples of the tool usage:
{bad_examples}

{format_instructions}
"""

IMPROVE_FIELD_DESCRIPTION = """
You are an AI Agent Tool developer can you make the description of a tool more precise and clear.
The name of the field is: {field_name}
The description of the field is: {field_description}

Please provide just the new description of the field. The new description shouldn't be longer than 30 words.

{format_instructions}
"""


class FixedDescriptionResponse(BaseModel):
    problems_with_current_description: str = Field(
        description="The reason for the failures with the current description.")
    how_to_avoid: str = Field(description="How to avoid the failures with the current description.")
    description: str = Field(description="The improved description of the tool.")


class ToolFixer:
    """
    Class to fix tool based on the bad examples found from running our fuzzing on the tool.
    """

    def __init__(self, tool):
        self.tool = tool
        self.tool_extractor = LangchainToolWrapper(tool)

        llm = init_model('gpt-4o', temperature=0.7)
        parser = PydanticOutputParser(pydantic_object=FixedDescriptionResponse)
        desc_prompt = PromptTemplate(template=IMPROVE_DESCRIPTION_TEMPLATE, input_variables=['tool_description'],
                                     partial_variables={'format_instructions': parser.get_format_instructions()})
        desc_src_prompt = PromptTemplate(template=IMPROVE_DESCRIPTION_SRC_TEMPLATE,
                                         input_variables=['tool_description', 'tool_source_code'],
                                         partial_variables={'format_instructions': parser.get_format_instructions()})
        desc_bad_ex_prompt = PromptTemplate(template=IMPROVE_DESCRIPTION_EXAMPLES_TEMPLATE,
                                            input_variables=['tool_description', 'bad_examples'],
                                            partial_variables={'format_instructions': parser.get_format_instructions()})

        field_prompt_examples = PromptTemplate(template=IMPROVE_FIELD_DESCRIPTION_EXAMPLES,
                                               input_variables=['field_name', 'field_description', 'bad_examples'],
                                               partial_variables={
                                                   'format_instructions': parser.get_format_instructions()})

        field_prompt = PromptTemplate(template=IMPROVE_FIELD_DESCRIPTION,
                                      input_variables=['field_name', 'field_description'],
                                      partial_variables={'format_instructions': parser.get_format_instructions()})

        self.chain_desc = desc_prompt | llm | parser
        self.chain_desc_src = desc_src_prompt | llm | parser
        self.chain_desc_ex = desc_bad_ex_prompt | llm | parser
        self.chain_field_ex = field_prompt_examples | llm | parser
        self.chain_field = field_prompt | llm | parser

    def fix(self):
        """
        Fix the tool based on just the description it has at the moment.
        """
        return self.chain_desc.invoke({'tool_description': self.tool_extractor.get_tool_information()})

    def fix_src(self):
        """
        Fix the tool based on the source code of the tool.
        """
        return self.chain_desc_src.invoke({'tool_description': self.tool_extractor.get_tool_information(),
                                           'tool_source_code': self.tool_extractor.get_tool_src()})

    def fix_bad_examples(self, bad_examples_file):
        """
        Fix the tool based on the bad examples found from running our fuzzing on the tool.
        """
        prompt_examples = self.__load_bad_examples(bad_examples_file)
        examples_size = len(prompt_examples)
        if examples_size == 0:
            raise Exception(f"No bad examples found for the tool {self.tool_extractor.get_tool_name()}")
        for example_count in [examples_size, int(0.75 * examples_size), int(0.5 * examples_size),
                              int(0.25 * examples_size),
                              int(0.1) * examples_size, 1]:
            result = self.try_return(prompt_examples, example_count)
            if result is not None:
                return result

    def try_return(self, prompt_examples, max_examples):
        try:
            return self.chain_desc_ex.invoke(
                {'tool_description': self.tool_extractor.get_tool_information(),
                 'tool_source_code': self.tool_extractor.get_tool_src(),
                 'bad_examples': self.__to_bad_examples_prompt(prompt_examples, max_examples)})
        except Exception as e:
            print(f"Exception for {max_examples} examples: {e}")
            return None

    def fix_fields(self):
        fields = self.tool.args_schema.__fields__
        fixed_fields = {}
        for field_name, field_model in fields.items():
            description = field_model.description
            # Now we need to fix the description:
            fixed_description = self.chain_field.invoke({'field_name': field_name, 'field_description': description})
            fixed_fields[field_name] = fixed_description
        return fixed_fields

    def fix_fields_examples(self, bad_examples_file):
        bad_examples = self.__load_bad_examples(bad_examples_file)
        fields = self.tool.args_schema.__fields__
        fixed_fields = {}
        for field_name, field_model in fields.items():
            description = field_model.description
            # Now we need to fix the description:
            samples = len(bad_examples) if len(bad_examples) < 5 else 5
            fixed_description = self.chain_field.invoke({'field_name': field_name, 'field_description': description,
                                                         'bad_examples': self.__to_bad_examples_prompt(bad_examples,
                                                                                                       samples)})
            fixed_fields[field_name] = fixed_description
        return fixed_fields

    def __load_bad_examples(self, bad_examples_file):
        with open(bad_examples_file, 'r') as f:
            bad_examples = json.loads(f.read())

        bad_examples = [PromptSetTestResults.model_validate(bad_ex) for bad_ex in bad_examples]
        # filter out only for our tool:
        bad_examples = [bad_ex for bad_ex in bad_examples if bad_ex.tool == self.tool_extractor.get_tool_name()]

        prompt_examples = []
        for bad_ex in bad_examples:
            bad_prompts = []
            good_prompts = []
            for run in bad_ex.individual_run_test_results:
                if run.unexpected_agent_output < 5 and bad_ex.tool_output_inconsistency and bad_ex.tool_arguments_inconsistency:
                    bad_prompts.append(run)
                elif run.unexpected_agent_output > 5 and (not run.tool_failure):
                    good_prompts.append(run)
            if len(bad_prompts) > 0 and len(good_prompts) > 0:
                prompt_examples.append((bad_prompts, good_prompts[0]))
            elif len(bad_prompts) > 0:
                prompt_examples.append((bad_prompts, None))
        return prompt_examples

    @staticmethod
    def __to_bad_examples_prompt(bad_examples: List[TestResult], max_examples: int):
        samples = random.sample(bad_examples, max_examples)
        result = ""
        for sample in samples:
            bad_samples = sample[0]
            bad_samples_str = '\n'.join(
                [f"Prompt: {bad_sample.prompt} resulting in bad args {bad_sample.tool_arguments}" for
                 bad_sample in bad_samples])
            if sample[1] is None:
                result += f"The following prompts are FAILING: {bad_samples_str}\n"
            else:
                good_sample = sample[1]
                example_string = f"""
    The following prompts are FAILING: {bad_samples_str}
    While the following prompt is PASSING: {good_sample.prompt} because it results to args {good_sample.tool_arguments}"""
                result += example_string + "\n"
        return result.strip()


if __name__ == '__main__':
    shell_tool = ShellToolLoader().get_tool()
    for i in range(50):
        new_desc = ToolFixer(shell_tool).fix_bad_examples(
            '/local/home/imilev/agent-tool-testing/src/test/result_terminal.json')
        print(new_desc.problems_with_current_description)
        print(new_desc.how_to_avoid)
        print(new_desc.description)
        with open(f'./fixed_desc_baseline_TD_SRC_{i}.txt', 'a') as f:
            f.write(new_desc.description.strip())
        print(f'{i}-----------------------------------')
