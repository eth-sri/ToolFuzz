from langchain.agents import AgentType
from langchain_experimental.agents import create_csv_agent

from src.toolfuzz.agent_executors.langchain.react_old import ReactAgentOld


class CsvAgent(ReactAgentOld):

    def __init__(self, csv, model):
        super().__init__(csv, model)
        self.agent = create_csv_agent(model, csv, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True,
                                      allow_dangerous_code=True, return_intermediate_steps=True)

    def get_name(self) -> str:
        return 'csv_agent'


class JsonAgent(ReactAgentOld):
    def __init__(self, json_spec, model):
        from langchain_community.tools.json.tool import JsonSpec
        from langchain_community.agent_toolkits import create_json_agent
        from langchain_community.agent_toolkits import JsonToolkit

        import yaml

        super().__init__(json_spec, model)
        with open(json_spec) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        json_spec = JsonSpec(dict_=data, max_value_length=4000)
        json_toolkit = JsonToolkit(spec=json_spec)

        self.agent = create_json_agent(llm=model, toolkit=json_toolkit, verbose=True)

    def get_name(self) -> str:
        return 'json_agent'
