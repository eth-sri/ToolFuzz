from typing import Optional, Type

from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_core.callbacks import CallbackManagerForToolRun
from pydantic import BaseModel, Field
from langchain_core.tools import BaseTool

ORIGINAL_DESCRIPTION = ("A wrapper around Wikipedia. "
                        "Useful for when you need to answer general questions about "
                        "people, places, companies, facts, historical events, or other subjects. "
                        "Input should be a search query.")

GOOD_DESCRIPTION = """A wrapper around Wikipedia. Useful for when you need to answer general questions about people, places, companies, facts, historical events, or other subjects. Input should be a search query.
The input should be the concrete event i.e. for: 
Question: What is the significance of French Revolution in history?, What is the significance of 1789 Revolution in history? 
Query:French revolution
Question: How did Industrial Development impact City Growth?, How did Industrial Growth impact Urban Development?
Query: Industrialization and urbanization
"""


class WikipediaQueryInput(BaseModel):
    """Input for the WikipediaQuery tool."""

    query: str = Field(description="query to look up on wikipedia")


class WikipediaQueryRunFixed(BaseTool):
    """Tool that searches the Wikipedia API."""

    name: str = "wikipedia"
    description: str = GOOD_DESCRIPTION
    api_wrapper: WikipediaAPIWrapper

    args_schema: Type[BaseModel] = WikipediaQueryInput

    def _run(
            self,
            query: str,
            run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the Wikipedia tool."""
        return self.api_wrapper.run(query)
