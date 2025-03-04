import random
import re

from src.toolfuzz.correctness.prompt_generation.llm_responses import AgentTemplatePrompts, AgentTemplateArguments, \
    LLMExpectedAnswers, LLMExpectedAnswer, PromptSimplification
from src.toolfuzz.correctness.prompt_generation.prompts import template_question, synonym_prompt, \
    llm_expectation_summary_prompt, \
    llm_answers_prompt, humanize_prompt
from src.toolfuzz.logging_mixin import LoggingMixin
from src.toolfuzz.prompt_generation.prompt_generator import PromptGenerator


class CorrectnessPromptGenerator(PromptGenerator, LoggingMixin):

    def __init__(self, tool_extractor, tool_context, model_name='gpt-4o', temperature=0.4):
        LoggingMixin.__init__(self)
        PromptGenerator.__init__(self, tool_extractor, model_name, temperature)
        self.prompt = template_question
        self.synonym_prompt = synonym_prompt
        self.llm_expectations = llm_expectation_summary_prompt
        self.answer_prompt = llm_answers_prompt
        self.generated_args = []
        self.tool_context = tool_context

    def generate_prompt(self, bad_arguments=None):
        res = self._generate_from_template(self.prompt, ['tool_prompt', 'tool_context'],
                                           {"tool_prompt": self.tool_prompt, 'tool_context': self.tool_context},
                                           AgentTemplatePrompts)
        assert 'template_prompts' in res
        # Now for each questions get the diffs:
        templates = res['template_prompts']
        for template in templates:
            prompt_args = self._generate_from_template(self.synonym_prompt,
                                                       ['template_prompt', 'tool_prompt', 'used_args', 'tool_context'],
                                                       {"template_prompt": template, "tool_prompt": self.tool_prompt,
                                                        "used_args": self.generated_args,
                                                        "tool_context": self.tool_context},
                                                       AgentTemplateArguments)
            self.update_gen_args(prompt_args)
            prompts = self.to_prompts(template, prompt_args)
            if len(prompts) > 4:
                prompts = self.humanize_prompts(prompts)
            answers = self._generate_from_template(self.answer_prompt, ['questions', 'tool_prompt'],
                                                   {'questions': '\n'.join(prompts),
                                                    'tool_prompt': self.tool_prompt},
                                                   LLMExpectedAnswers)
            llm_expectation = self._generate_from_template(self.llm_expectations, ['sentences'],
                                                           {'sentences': '\n'.join(
                                                               answers['expected_answers'])},
                                                           LLMExpectedAnswer)
            if isinstance(llm_expectation, dict) and 'expected_answer' in llm_expectation:
                yield template, prompts, llm_expectation['expected_answer']
            else:
                yield template, prompts, llm_expectation

    def humanize_prompts(self, prompts):
        indx_list = list(range(len(prompts)))
        selection = random.sample(indx_list, int(len(prompts) / 2))
        humanized_prompts = [prompts[i] for i in selection]
        humanized_prompts = self._generate_from_template(humanize_prompt, ['tool_prompt', 'prompts'],
                                                         {'tool_prompt': self.tool_prompt,
                                                          'prompts': humanized_prompts},
                                                         PromptSimplification)['simplified_prompts']
        for i in range(len(prompts)):
            if i in selection:
                prompts[i] = humanized_prompts.pop(0)
            else:
                prompts[i] = prompts[i]

        return prompts

    def update_gen_args(self, prompt_args):
        # Get just the first two
        for args in prompt_args['template_arguments']:
            self.generated_args += args['argument_values'][:2]

    def to_prompts(self, template, prompt_args):
        str_template = re.sub('\[.*?\]', '{}', template)
        arguments = prompt_args['template_arguments']
        str_args_sets = []
        for i in range(len(arguments[0]['argument_values'])):
            str_args = []
            for argument in arguments:
                str_args.append(argument['argument_values'][i])
            if len(str_args_sets) != 0 and len(str_args_sets[-1]) == len(str_args):
                str_args_sets.append(str_args)
            if len(str_args_sets) == 0:
                str_args_sets.append(str_args)

        # now yield the results
        prompts = [str_template.format(*str_args_set) for str_args_set in str_args_sets]
        prompts = [prompt for prompt in prompts if len(re.findall('\[.*?\]', prompt)) == 0]
        if len(prompts) == 0:
            self.log_debug(f"WARN: couldn't infill template: {template}, arguments: {arguments}")
        return prompts
