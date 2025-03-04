from typing import List

from pydantic import BaseModel


class Bucket(BaseModel):
    bucket_items: List[str]
    bucket_value: str


class TestResult(BaseModel):
    prompt: str
    tool_arguments: str
    tool_output: str
    agent_output: str
    tool_failure: bool
    unexpected_agent_output: int
    agent_output_not_relevant: bool
    llm_agent_out_reason: str
    trace: str


class PromptSetTestResults(BaseModel):
    tool: str
    template_question: str
    llm_output_expectation: str
    template_prompts: List[str]
    same_arguments_buckets: List[Bucket]
    same_output_buckets: List[Bucket]
    tool_arguments_inconsistency: bool
    tool_output_inconsistency: bool
    individual_run_test_results: List[TestResult]


class TestFailureResult(BaseModel):
    tool: str
    invocation_params: str
    fuzzed_params: str
    expected_exception: str
    exception: str
    prompt: str
    agent_type: str
    trace: str
    successful_trigger: bool
