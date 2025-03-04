from src.toolfuzz.prompt_generation.prompt_generator import PromptGenerator
from src.toolfuzz.runtime.prompt_generation.llm_responses import BadArgumentsPromptResponse
from src.toolfuzz.runtime.prompt_generation.prompts import prompt_from_arguments_prompt


class RuntimeFailurePromptGeneration(PromptGenerator):
    def __init__(self, tool_extractor, model='gpt-4o', temperature=0):
        super().__init__(tool_extractor, model, temperature)
        self.prompt = prompt_from_arguments_prompt

    def generate_prompt(self, bad_arguments):
        res = self._generate_from_template(self.prompt, ['tool_prompt', 'query'],
                                           {"tool_prompt": self.tool_prompt, "bad_args": bad_arguments},
                                           BadArgumentsPromptResponse)
        assert 'prompts' in res
        return res['prompts']
