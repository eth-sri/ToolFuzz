from src.eval.buggy_tools.open_street_map import open_street_map_distance, open_street_map_search
from src.eval.toolfuzz.loaders.langchain_loader import ReactNewAgentLoader


class CustomToolsLoader(ReactNewAgentLoader):
    def __init__(self, name):
        self.tool_name = name

    def get_tool(self):
        tools = {
            'open_street_map_distance': open_street_map_distance,
            'open_street_map_search': open_street_map_search
        }

        return tools[self.tool_name]

    def can_load(self, tool: str) -> bool:
        return tool.lower() in ['open_street_map_distance', 'open_street_map_search']
