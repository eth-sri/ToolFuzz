def assert_contains(self, agent_invoke, prompt, contains_text):
    last_msg = None
    is_tool_called = False
    for step in agent_invoke(prompt):
        if check_if_tool_call(step):
            is_tool_called = True
        last_msg = step

    self.assertTrue(is_tool_called, "Agent did NOT invoke tool.")
    agent_output = get_output(last_msg)

    contains_text = str(contains_text)
    self.assertIn(contains_text.lower(), agent_output.lower())


def assert_tool_call(self, agent_invoke, prompt):
    is_tool_called = False
    for step in agent_invoke(prompt):
        if check_if_tool_call(step):
            is_tool_called = True
    self.assertTrue(is_tool_called, "Agent did NOT invoke tool.")


def check_if_tool_call(step):
    if 'agent' in step and 'messages' in step['agent'] and \
            'tool_calls' in step['agent']['messages'][0].additional_kwargs:
        return True
    if 'actions' in step and len(step['actions']) != 0:
        return True
    return False


def get_output(agent_output):
    if 'output' in agent_output:
        return str(agent_output['output'])
    if 'agent' in agent_output and 'messages' in agent_output['agent']:
        return str(agent_output['agent']['messages'][-1].content)
    raise ValueError(f"Unknown agent output format {agent_output}")
