import json

from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.tools import ToolException
from langchain_openai import ChatOpenAI
from tqdm import tqdm

from src.eval.toolfuzz.envs.reset_context import DummyResetContext, ResetContext
from src.toolfuzz.agent_executors.agent_executor import TestingAgentExecutor
from src.toolfuzz.correctness.correctness_oracle import CorrectnessOracle
from src.toolfuzz.correctness.prompt_generation.prompt_generator import CorrectnessPromptGenerator
from src.toolfuzz.dataclasses import TestResult, PromptSetTestResults
from src.toolfuzz.logging_mixin import LoggingMixin
from src.toolfuzz.tools.info_extractors.tool_wrapper_factory import ToolWrapperFactory
from src.toolfuzz.utils import save_test_results, save_test_results_html


class CorrectnessTester(LoggingMixin):
    def __init__(self, llm, tool,
                 agent: TestingAgentExecutor,
                 additional_context: str = '',
                 custom_tool_wrapper=None,
                 context_resetter: ResetContext = DummyResetContext(),
                 prompt_set_iters=10):
        super().__init__()
        self.tool, self.agent = tool, agent
        self.context = additional_context
        self.model = llm
        if isinstance(self.model, str):
            self.model = ChatOpenAI(model=self.model)

        self.prompt_set_iters = prompt_set_iters
        self.results = []
        self.context_resetter = context_resetter
        self.tool_extractor = ToolWrapperFactory.create_extractor(tool) \
            if custom_tool_wrapper is None else custom_tool_wrapper

    def test(self):
        oracle = CorrectnessOracle()
        prompt_set_iters = 0

        prompt_gen = CorrectnessPromptGenerator(self.tool_extractor, self.context)
        while True:
            prompts = prompt_gen.generate_prompt()
            for template, prompt_set, llm_expect in tqdm(prompts, desc='Testing prompt sets'):
                print(f"({prompt_set_iters}/{self.prompt_set_iters}) Testing prompt set: {template}")
                if prompt_set_iters >= self.prompt_set_iters:
                    # The number of prompt sets to test has been reached
                    return

                prompt_set_iters += 1
                outs = []
                individual_test_results = []
                for prompt in tqdm(prompt_set, desc="Running prompt set"):
                    self.log_info(f"Prompt: {prompt}")
                    if len(prompt) == 0:
                        continue
                    agent_result, test_res = self.run_prompt(prompt)
                    if agent_result is None:
                        individual_test_results.append(test_res)
                    else:
                        outs.append((agent_result, prompt))

                tool_output_inconsistency, output_buckets = oracle.evaluate_tool_output(outs)
                tool_arguments_inconsistency, args_buckets = oracle.evaluate_tool_arguments(outs)

                for agent_res, prompt in outs:
                    if isinstance(agent_res.tool_output, str):
                        tool_out_str = agent_res.tool_output
                    elif isinstance(agent_res.tool_output, list):
                        tool_out_str = '\n'.join(agent_res.tool_output)
                    else:
                        tool_out_str = str(agent_res.tool_output)
                    correctness_degree, reason = oracle.agent_out_correctness(agent_res.agent_response,
                                                                              tool_out_str,
                                                                              llm_expect)
                    agent_output_relevant = True
                    if correctness_degree < 5 and not tool_output_inconsistency:
                        agent_output_relevant, _ = oracle.is_agent_output_relevant(agent_res.agent_response, prompt,
                                                                                   tool_out_str, llm_expect)
                    individual_test_results.append(
                        TestResult(prompt=prompt, tool_arguments=self.tool_args_str(agent_res.tool_args),
                                   tool_output=tool_out_str,
                                   agent_output=agent_res.agent_response,
                                   tool_failure=agent_res.is_raised_exception,
                                   unexpected_agent_output=correctness_degree,
                                   agent_output_not_relevant=(not agent_output_relevant),
                                   llm_agent_out_reason=reason,
                                   trace=json.dumps(agent_res.trace, default=callback_manager_serializer)))

                self.results.append(
                    PromptSetTestResults(tool=self.tool_extractor.get_tool_name(), template_question=template,
                                         template_prompts=prompt_set,
                                         same_arguments_buckets=args_buckets,
                                         same_output_buckets=output_buckets,
                                         tool_arguments_inconsistency=tool_arguments_inconsistency,
                                         tool_output_inconsistency=tool_output_inconsistency,
                                         llm_output_expectation=llm_expect,
                                         individual_run_test_results=individual_test_results))

    def run_prompt(self, prompt):
        try:
            agent_result = self.agent(prompt)
            return agent_result, None
        except ToolException as e:
            return None, TestResult(prompt=prompt, tool_arguments='Invalid tool call', tool_output="Tool FAILURE",
                                    agent_output=f"Tool Failure {e}",
                                    tool_failure=True,
                                    unexpected_agent_output=0,
                                    agent_output_not_relevant=True,
                                    llm_agent_out_reason="Tool Failure",
                                    trace="{}")
        finally:
            self.context_resetter.reset_context()

    @staticmethod
    def tool_args_str(args):
        if type(args) == str:
            return args
        if type(args) == dict:
            return str({k: v for k, v in args.items() if k != 'run_manager'})
        return str(args)

    def save(self, file_name='./results_correctness'):
        save_test_results(self.results, f"{file_name}.json")
        save_test_results_html(self.results, f"{file_name}.html")


def callback_manager_serializer(obj):
    if isinstance(obj, CallbackManagerForToolRun):
        return ""  # Replace non-serializable objects with an empty string

    # Use the default behavior happen for other objects
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")
