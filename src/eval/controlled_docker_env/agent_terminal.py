from langchain_community.tools import ShellTool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent


def setup():
    model = ChatOpenAI(model='gpt-4o-mini', temperature=0)
    shell_tool = ShellTool()
    with open('/agentworkspace/tool_description.txt', 'r') as f:
        shell_tool.description = f.read().strip()
    return create_react_agent(model, [shell_tool])


def main():
    # Run the terminal thing
    agent = setup()
    with open('/agentworkspace/prompt.txt', 'r') as f:
        prompt = f.read()
    prompt = "You should know that you are operating in the home directory: /, but the workspace is in /agentworkspace/workfiles." + prompt
    result = agent.invoke({'messages': [HumanMessage(content=prompt)]})
    print(result)


if __name__ == '__main__':
    main()
