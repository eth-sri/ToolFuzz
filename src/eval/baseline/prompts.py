prompt_crash = """
You are an AI assistant tester. The idea is to come up with prompts which will make the following tool crash.
Example:
Tool information: This tool can divide two numbers.
Crash prompts: [
"Can you please divide 10 by 0",
"If I have no friends left how can I divide my apples evenly between them?"
]

Tool information: {tool_info}
Now generate the crash prompts, you MUST give the full string prompt and no further logic has to be ran on these prompts. I.e. NO "a"+"b" or other similar logic.
{format_instructions}
"""

prompt_correctness = """
You are an AI assistant tester. The idea is to come up with prompts which will make the following tool produce incorrect answer.
Tool information: {tool_info}

Please generate prompts which will make the following tool produce incorrect answer.
{format_instructions}
"""

prompt_oracle = """
You are an AI assistant judge. Your job is to evaluate and reason on the correctness of the given answer knowing the question is:
{question}
The provided answer is: {answer}

Is the answer correct, please provide reasoning?
{format_instructions}
"""
