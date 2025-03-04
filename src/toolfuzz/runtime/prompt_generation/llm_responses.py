from typing import List

from pydantic import BaseModel, Field


class BadArgumentsPromptResponse(BaseModel):
    prompts: List[str] = Field(
        description="Multiple prompts which can trigger Agent tool usage with predefined parameters")
