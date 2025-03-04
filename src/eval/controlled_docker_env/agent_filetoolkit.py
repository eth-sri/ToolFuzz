from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent


def setup():
    model = ChatOpenAI(model='gpt-4o-mini', temperature=0)
    toolkit = FileManagementToolkit(root_dir='/agentworkspace/workfiles')
    tools = toolkit.get_tools()
    tools = {tool.name: tool for tool in tools}

    with open('/agentworkspace/tool_description.txt', 'r') as f:
        # The lines follow exact structure of the tool descriptions
        lines = f.readlines()
        for line in lines:
            if len(line.strip()) != 0:
                tool_name = line.split(':')[0].strip()
                tools[tool_name].description = line.strip()
    return create_react_agent(model, list(tools.values()))


def main():
    # Run the terminal thing
    agent = setup()
    with open('/agentworkspace/prompt.txt', 'r') as f:
        prompt = f.read()
    result = agent.invoke({'messages': [SystemMessage(content="You are an AI agent operating with the file system."),
                                        HumanMessage(content=prompt)]})
    print(result)


if __name__ == '__main__':
    main()
