# Start from a minimal Alpine image
FROM alpine:3.18

ARG SETUP_FILE='setup.sh'
ARG PROMPT_FILE='prompt.txt'
ARG GROUND_TRUTH='./ground_truths/*'
ARG AGENT_FILE='./agent_terminal.py'
ARG TOOL_DESC='tool_description.txt'

ENV LANGCHAIN_TRACING_V2=FALSE
ENV LANGCHAIN_API_KEY=''
ENV OPENAI_API_KEY=''

# Install Python and other dependencies
# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 git && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# Copy and install requirements if you have a requirements.txt file
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir -p /agentworkspace/
RUN mkdir -p /agentworkspace/workfiles
RUN mkdir -p /agentworkspace/.git

COPY $AGENT_FILE /agentworkspace/agent.py
COPY $GROUND_TRUTH/.git /agentworkspace/workfiles/.git

COPY $SETUP_FILE /agentworkspace/setup.sh
COPY $PROMPT_FILE /agentworkspace/prompt.txt

COPY $TOOL_DESC /agentworkspace/tool_description.txt

RUN chmod +x /agentworkspace/setup.sh

CMD sh /agentworkspace/setup.sh /agentworkspace/workfiles && python3 /agentworkspace/agent.py && git -C /agentworkspace/workfiles status

