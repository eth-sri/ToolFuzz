from typing import List

from pydantic.v1 import BaseModel, Field


class AgentTemplatePrompts(BaseModel):
    template_prompts: List[str] = Field(
        description="List of prompt templates.")


class Argument(BaseModel):
    argument_values: List[str] = Field(description="Synonymous values for an argument.")


class AgentTemplateArguments(BaseModel):
    template_arguments: List[Argument] = Field(
        description="List of the arguments for a tool call. Each Argument is a list of synonymous values for "
                    "that one argument. The order of this list is according to the given template")


class LLMExpectedAnswers(BaseModel):
    expected_answers: List[str] = Field(description="The emulated answers that are returned by tool.")


class LLMExpectedAnswer(BaseModel):
    expected_answer: str = Field(
        description="The one answer which is representing most of the given sentences and is factually correct.")


class PromptSimplification(BaseModel):
    simplified_prompts: List[str] = Field(description="List of simplified prompts.")


class RelevanceResponse(BaseModel):
    is_relevant: bool = Field(description="Whether the model agrees or not that the answer is relevant to the question")
    reason: bool = Field(description="The reason behind the model's choice of the relevancy of the statement")


class CorrectnessResponse(BaseModel):
    correctness_degree: int = Field(
        description="to what extend does the model agree with the statement between 1 and 10. 1 Being the least and 10 meaning exactly what is expected")
    reason: str = Field(description="the reason behind the model's choice of the correctness of the statement")
