from src.eval.toolfuzz.information_provider import TestInformationProvider


def valid_prompt(prompt_text, assert_lambda):
    def decorator(func):
        if hasattr(func, 'valid_prompt'):
            func.breaking_prompt.append(TestInformationProvider(prompt_text, assert_lambda))
        else:
            func.__dict__['valid_prompt'] = [TestInformationProvider(prompt_text, assert_lambda)]
        return func

    return decorator


def breaking_prompt(prompt_text, assert_lambda):
    def decorator(func):
        if hasattr(func, 'breaking_prompt'):
            func.breaking_prompt.append(TestInformationProvider(prompt_text, assert_lambda))
        else:
            func.__dict__['breaking_prompt'] = [TestInformationProvider(prompt_text, assert_lambda)]
        return func

    return decorator


def tool_description(description):
    """
    Empty tool used to describe what is the usage of the tool
    :param description:
    :return: the original func
    """

    def dec(func):
        return func

    return dec
