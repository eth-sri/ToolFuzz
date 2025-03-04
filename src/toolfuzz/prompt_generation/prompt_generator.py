import abc

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


class PromptGenerator(abc.ABC):

    def __init__(self, tool_extractor, model='gpt-4o', temperature=0):
        self.tool_prompt = tool_extractor.get_tool_docs()
        self.model = ChatOpenAI(model=model, temperature=temperature)

    def _generate_from_template(self, template, template_vars, template_values, return_type):
        parser = JsonOutputParser(pydantic_object=return_type)
        prompt = PromptTemplate(template=template, input_variables=template_vars,
                                partial_variables={"format_instructions": parser.get_format_instructions()})
        chain = prompt | self.model | parser
        return chain.invoke(template_values)
