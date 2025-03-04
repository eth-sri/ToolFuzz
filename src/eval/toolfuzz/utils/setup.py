from langchain_openai import ChatOpenAI


def init_model(name, temperature=0):
    return ChatOpenAI(model=name, temperature=temperature)
