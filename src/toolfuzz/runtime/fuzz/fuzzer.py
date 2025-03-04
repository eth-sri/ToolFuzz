import asyncio
import inspect
import json

from src.toolfuzz.logging_mixin import LoggingMixin
from src.toolfuzz.runtime.fuzz.taints import TaintDict, TaintStr
from src.toolfuzz.runtime.fuzz.type_generators import StringGenerator, get_generators
from src.toolfuzz.tools.info_extractors.langchain_tool_wrapper import LangchainToolWrapper


class Fuzzer(LoggingMixin):
    def __init__(self, tool, max_iterations=100, custom_tool_extractor=None):
        super().__init__()
        self.tool_extractor = LangchainToolWrapper(tool) if custom_tool_extractor is None else custom_tool_extractor
        self.max_iterations = max_iterations
        self.tool_args = self.tool_extractor.get_tool_args()
        self.tool = tool
        self.generators = get_generators()
        self.str_seed = TaintStr(''), TaintStr('{}')

    def generate_tool_kwargs(self, iter):
        arguments = {}
        for arg in self.tool_args:
            arg_generator = None
            for gen in self.generators:
                if gen.can_gen(arg.type):
                    arg_generator = gen
                    break
            if arg_generator is None:
                assert arg.has_default, f'No argument generator found for {arg}. Available generators {self.generators}. Tool {self.tool}'
                continue

            if iter < len(self.str_seed) and isinstance(arg_generator, StringGenerator):
                arguments[arg.name] = self.str_seed[iter]
            else:
                arguments[arg.name] = arg_generator.generate(arg.type, iter % 100 == 0)  # every 20 iters change
        return arguments

    def fuzz(self):
        self._clear_state()
        bad_params = {}
        with CustomJsonParseBlock():
            for iter in range(self.max_iterations):
                kwargs = self.generate_tool_kwargs(iter)
                try:
                    self.log_info(f"({iter}/{self.max_iterations}) Generated args {kwargs}")
                    self.tool_extractor.invoke_tool(kwargs)
                except Exception as e:
                    exception_type = type(e)
                    if exception_type in bad_params:
                        bad_params[exception_type].append(kwargs)
                    else:
                        bad_params[exception_type] = [kwargs]
            return bad_params

    @staticmethod
    def _clear_state():
        TaintDict.acc_keys = []


def load_in_taint_dict(dictionary):
    return TaintDict(dictionary)


class CustomJsonParseBlock:
    def __init__(self):
        self.original_json_loads = json.loads

    def __enter__(self):
        def custom_json_loads(*args, **kwargs):
            return self.original_json_loads(object_hook=load_in_taint_dict, *args, **kwargs)

        json.loads = custom_json_loads

    def __exit__(self, exc_type, exc_val, exc_tb):
        json.loads = self.original_json_loads
