from typing import Any
import json

from langchain_openai import ChatOpenAI
from tqdm import tqdm

from src.eval.toolfuzz.envs.reset_context import DummyResetContext, ResetContext
from src.toolfuzz.agent_executors.agent_executor import TestingAgentExecutor
from src.toolfuzz.dataclasses import TestFailureResult
from src.toolfuzz.logging_mixin import LoggingMixin
from src.toolfuzz.runtime.fuzz.fuzzer import Fuzzer
from src.toolfuzz.runtime.prompt_generation.prompt_generator import RuntimeFailurePromptGeneration
from src.toolfuzz.tools.info_extractors.tool_wrapper import ToolWrapper
from src.toolfuzz.tools.info_extractors.tool_wrapper_factory import ToolWrapperFactory
from src.toolfuzz.utils import save_test_results, save_test_results_html


class RuntimeErrorTester(LoggingMixin):
    def __init__(self,
                 llm,
                 tool: Any,
                 agent: TestingAgentExecutor,
                 custom_tool_wrapper: ToolWrapper = None,
                 context_resetter: ResetContext = DummyResetContext(),
                 bad_examples_per_param: int = 5,
                 fuzzer_iters: int = 10):
        super().__init__()
        self.model, self.agent, self.tool = llm, agent, tool
        if isinstance(self.model, str):
            self.model = ChatOpenAI(model=self.model)

        self.tool_extractor = ToolWrapperFactory.create_extractor(tool) \
            if custom_tool_wrapper is None else custom_tool_wrapper

        self.fuzzer = Fuzzer(self.tool,
                             max_iterations=fuzzer_iters,
                             custom_tool_extractor=self.tool_extractor)
        self.context_resetter = context_resetter
        self.test_results = []
        self.bad_examples = bad_examples_per_param

    def test(self):
        pg = RuntimeFailurePromptGeneration(self.tool_extractor)
        bad_arguments_w_exception = self.fuzzer.fuzz()
        caught_exceptions = set()
        for exception, bad_arguments in tqdm(bad_arguments_w_exception.items(), desc='Testing for exceptions'):
            for i in range(0, len(bad_arguments)):
                if exception in caught_exceptions:
                    break

                bad_arg_examples = bad_arguments[i]
                pre_check = self.sanity_check(self.agent, bad_arg_examples)
                if not pre_check:
                    continue
                prompts = pg.generate_prompt(bad_arg_examples)
                for prompt in prompts:
                    self.log_info(f'{prompt} for {bad_arg_examples}')
                    thrown_exception, test_result = self.run_test(self.agent, prompt, exception,
                                                                  self.tool_extractor.get_tool_name(),
                                                                  bad_arg_examples,
                                                                  self.agent.get_name())
                    self.test_results.append(test_result)
                    if thrown_exception:
                        caught_exceptions.add(thrown_exception)

    def run_test(self, runnable, prompt, expected_exception, tool_name, bad_args, agent_type):
        try:
            agent_result = runnable(prompt)
            if type(agent_result.exception) != str:
                agent_result.exception = str(type(agent_result.exception)) + str(agent_result.exception)
            return expected_exception, TestFailureResult(tool=tool_name,
                                                         expected_exception=str(expected_exception),
                                                         exception=agent_result.exception,
                                                         prompt=prompt, agent_type=agent_type,
                                                         invocation_params=agent_result.tool_args,
                                                         fuzzed_params=str(bad_args),
                                                         successful_trigger=agent_result.is_raised_exception,
                                                         trace=json.dumps(agent_result.trace))
        except expected_exception as e:
            return expected_exception, TestFailureResult(tool=tool_name,
                                                         expected_exception=str(expected_exception),
                                                         exception=str(type(e)) + str(e),
                                                         prompt=prompt, agent_type=agent_type,
                                                         invocation_params='Invocation was interrupted',
                                                         fuzzed_params=str(bad_args),
                                                         successful_trigger=True,
                                                         trace=json.dumps({'error': str(e)}))
        except Exception as e:
            return type(e), TestFailureResult(tool=tool_name,
                                              expected_exception=str(expected_exception),
                                              exception=str(type(e)) + str(e),
                                              prompt=prompt, agent_type=agent_type,
                                              fuzzed_params=str(bad_args),
                                              invocation_params='Invocation was interrupted',
                                              successful_trigger=True,
                                              trace=json.dumps({'error': str(e)}))
        finally:
            self.context_resetter.reset_context()

    def sanity_check(self, agent_callable, bad_args) -> bool:
        prompt = f"Please invoke the {self.tool_extractor.get_tool_name()} exactly like: {self.tool_extractor.get_tool_declaration_name()}({bad_args})"
        try:
            response = agent_callable(prompt)
            return response.is_tool_invoked and response.is_raised_exception
        except Exception as e:
            self.log_info(f'Sanity check passed for {bad_args}: {e}')
            return True

    def save(self, file='./results_runtime'):
        save_test_results(self.test_results, f"{file}.json")
        save_test_results_html(self.test_results, f"{file}.html")
