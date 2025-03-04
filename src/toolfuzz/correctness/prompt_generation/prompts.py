template_question = \
    """Can you generate template questions according to a tool description. Here is an example on how to do so
Having a map tool which can give me distances between two places possible question templates are:
What is the distance from [A] to [B]?
How much time would it take to go from [A] to [B]?
If I start from [A] and go to [B] with [C] km/h average speed how much time would it take me?

For tools that are knowledge based i.e. news, fact stores etc. You can generate questions similar to:
What do you know about [A]?
What is/are [A] for [B]?
Is it true that [A] is [B]?
Is [A] related to [B]?
In what year did [A] happen?
When was [A] born?
Find [A] in [B]?
[A] my work to [B].
[A] from [B] to [C].

Also some more specific questions like: 
Is it true that Mr [A] was related to Mrs. [B]?
I am at [A], how much time it will take me to go from the closest [B] to the [C] airport? 
Find an article/paper/document written by [A] on topic [B]?

Now having a tool with description: '{tool_prompt}'
And the tool context: {tool_context}

Please generate templates, try to generate more specific templates.
{format_instructions}."""


synonym_prompt = \
    """"Imagine you are a user who is using an AI agent and just ask it in normal speech. 
Please generate appropriate template input values for the given template:
'{template_prompt}'
They should be related to the context of tool:
{tool_prompt}
And the tool context: {tool_context}
These inputs should be synonyms or different way of expressing the same thing. 

Here is an example:
Template: 'What are some [A] in [B]?'
Infills for A: ['Coffee Shop', 'Cafeteria', 'Coffeehouse', 'Café']
Infills for B: ['Zurich', 'ZH', 'Zurich Switzerland', 'ZH CH', 'ZH Switzerland', 'Zurich CH']

Template: 'Who is [A]?'
Infills for A: ['Albert Einstein', 'A. Einstein', 'Alb. Einstein', 'Einstein'] 

Template: 'When did [A] happen?'
Infills for A: ['World War I' , 'World War One', 'WW 1', 'First World War']

Template: 'What are the latest news in [A]?
Infills for A: ['cinema', 'hollywood', 'kino', 'movies', 'show business']

Template: 'What are the [A] in [B]?'
Infills for A: ['latest news', 'current events', 'breaking news', 'daily news', 'daily events']
Infills for B: ['politics', 'government', 'public affairs']

Template: 'I am at [A], how much time it will take me to go from the closest [B] to the [C]?'
Infills for A: ['Zurich HB', 'Zurich main train station', 'Zurich main station']
Infills for B: ['Mc Donalds', 'fast food restaurant McDonalds', 'McD burgers']
Infills for C: ['ETH HG Bibliothek', 'ETH main building library', 'ETH main library']

Template: 'Can you find [A] in [B]?'
Infills for A: ['family picture', 'png with the family', 'family photo', 'family portrait']
Infills for B: ['the home directory', 'my workspace', 'main directory']

Template: '[A] [B] to [C]'
Infills for A: ['Submit', 'Send', 'Upload', 'Commit']
Infills for B: ['main.py', 'the main python file', 'src/main', 'the main source file']
Infills for C: ['the server', 'the cloud', 'the repository', 'the remote branch']

Template: '[A] my work to [B]'
Infills for A: ['Move', 'Transfer', 'Cut']
Infills for B: ['archive folder', 'the archive']

Please DO NOT use any of the already generated examples: {used_args}.

{format_instructions}."""


humanize_prompt = """
Given the following tool description: '{tool_prompt}' and the following tool prompts that are synonymous: '{prompts}'
Please make such that the prompts are like a person would write it and not a machine, so nothing too concrete but also not too vague.

{format_instructions}"""


llm_answers_prompt = \
    """You are emulating the following tool: {tool_prompt}. Given the tool return value for the following questions:
{questions}

Example:
Tool description: Tool which can find a route between two locations and give back the distance in km of that route. The route is on rodes that can be driven with car. The tool provides route distance in km for car trip between the two locations.
The two locations can be cities or concrete places i.e. office buildings, shops, parks and so on.

Questions:
What is the distance between Sofia and Zurich?
What is the distance between SF and ZH?
What is the distance between Sofia BG and Zurich CH?
What is the distance between Sofia Bulgaria and Zurich Switzerland?

Answers:
The road distance between Sofia, Bulgaria, and Zurich, Switzerland is approximately 1,450 kilometers (900 miles).
If "SF" refers to San Francisco (SF), California, USA and "ZH" refers to Zurich (ZH), Switzerland, the distance is vast. Since it's impossible to drive directly due to the Atlantic Ocean, the driving distance would be irrelevant. However, hypothetically driving the distance across land would exceed 9,500 kilometers (5,900 miles).
"BG" stands for Bulgaria and "CH" stands for Switzerland. The road distance between Sofia, Bulgaria, and Zurich, Switzerland is approximately 1,450 kilometers (900 miles)
The road distance between Sofia, Bulgaria, and Zurich, Switzerland is about 1,450 kilometers (900 miles).

{format_instructions}."""


llm_expectation_summary_prompt = \
    """You have the following sentences:
{sentences}
Make once sentence which is factually correct to you and most of the sentences, not required to represent all of the answer but MUST be approximately correct.

Examples:

Sentences:
The road distance between Sofia, Bulgaria, and Zurich, Switzerland is approximately 1,450 kilometers (900 miles).
If "SF" refers to San Francisco (SF), California, USA and "ZH" refers to Zurich (ZH), Switzerland, the distance is vast. Since it's impossible to drive directly due to the Atlantic Ocean, the driving distance would be irrelevant. However, hypothetically driving the distance across land would exceed 9,500 kilometers (5,900 miles).
"BG" stands for Bulgaria and "CH" stands for Switzerland. The road distance between Sofia, Bulgaria, and Zurich, Switzerland is approximately 1,450 kilometers (900 miles)
The road distance between Sofia, Bulgaria, and Zurich, Switzerland is about 1,450 kilometers (900 miles).
Answer: The expected distance is around 1500 kilometers.
{format_instructions}."""

relevance_prompt = \
    """You are assessing an agent RESPONSE. You should give an answer of either true if the response is related to the asked question or false otherwise. Alongside the evaluation of true/false you should provide reasoning for it.
Use the following examples as reference:

#Example 1:
Question: Can you list the current directory?
Agent response: drwxr-xr-x 13 imilev imilev 4096 Jul  8 15:33 Workspace
drwxr-xr-x 19 imilev imilev 4096 Feb 14  2024 miniconda3
drwxr-xr-x  3 imilev imilev 4096 Sep 18  2023 nltk_data
Expectations:
1. drwxr-xr-x   3 root root   4096 Sep 25  2023 Docker
lrwxrwxrwx   1 root root      7 May  1  2023 bin -> usr/bin
drwxr-xr-x   2 root root   4096 Apr 18  2022 boot
drwxr-xr-x   9 root root   2800 Aug 15 10:49 dev
drwxr-xr-x  89 root root   4096 Aug 15 10:50 etc
drwxr-xr-x   3 root root   4096 Jul 10  2023 home
2. Get a list of files in the ls command output format.
Is relevant: true
Reason: Even thou the answer is not the same as the expectation it still lists files so it is relevant.


#Example 2:
Question:What is the distance from Zurich to Sofia?
Agent Response:The distance from Zurich to Sofia is approximately 10,811 kilometers.
Expectations:
1. The distance between Zürich to Sofia is 10810927.1 meters
2. The road distance between Zurich, Switzerland, and Sofia, Bulgaria, is approximately 1,450 kilometers (900 miles).
Is relevant:false
Reason:The answer does not comply with the second expectation.

Now please evaluate the following example:
Agent Response: {agent_out}
Question:{question}
Expectations:
1. {tool_output}
2. {llm_expect}

{format_instructions}"""


correctness_prompt = \
    """"You are assessing an agent RESPONSE. You should give an between 1 and 10. 10 means that the answer satisfies both criteria: first is the tool output and second is LLM expectation, the agent response should be within 10% margin of error or false otherwise. 0 is for when both criteria are not satisfied
Alongside the evaluation of true/false you should provide reasoning for it.

Use the following examples as reference:
#Example 1:
Agent response: The capital city of France is Paris
Expectations:
1. No results found for the query
2. Paris
correctness_degree: 5
Reason: The response doesn't comply with the first expectation: 'No results found for the query
    
#Example 2:
Agent response: As of now, the current survey results for the 2024 US presidential election show Kamala Harris leading Donald Trump. Here are the key figures:\n\n- **Kamala Harris**: 46%\n- **Donald Trump**: 48%\n- **Robert F. Kennedy Jr.**: 5.5%\n\nHarris's popularity has seen a significant increase, with half of voters viewing her favorably, which is an improvement from 43% the previous week.
Expectations:
1.Kamala Harris, Donald Trump.
2.The current survey results for the 2024 US presidential election show candidate A leading with X%, followed by candidate B with Y%, and other candidates with Z% and W%.
correctness_degree: 9
Reason: The response mentions both Kamala Harris and Donal Trump thus complying with the first expectation and also presents percentages and thus complying with the second.
    
Example 3:
Agent response: If you're looking for a solid, mid-range option, expect to spend around $400 to $500, there is one cheaper option around 350 USD
Expectation:
1.$347.99
2.A TV sells in the range of 400-800 USD" +
correctness_degree: 8
Reason: The response is close enough to the expected values and is based on the expected tool output"

Example 4:
Agent response: The distance between LA and Sofia is 1,047 miles
Expectation:
1. Distance from Sofia to LA is 10,633 km
2. The distance between Sofia and LA is 10 000 KM
correctness_degree: 2
Reason: The response doesn't comply with both expectations - the error is too big, but is still mentioning the correct names.

Now please evaluate the following agent response and give the reason for your evaluation: 
'{agent_output}'
Expectations:
1.{tool_output}
2.{expected}
{format_instructions}"""


tool_output_correctness = \
    """You are assessing a tool output which was called via an Large Language Model agent.
You should give an answer of either true if the given answer satisfies the expectation, or false otherwise.
Alongside this evaluation please provide your reasoning for it.
Expectation:
{expected}


Use the following examples as reference:

#Example 1:
Tool output:The car travel distance between Berlin Central Station and Munich Central Station is approximately 583.9 kilometers
Expectation:The distance between Berlin Central Station to Munich Central Station is 583862.4 meters
Is correct: true
Reason: 583.9 kilometers is approximately the same as 583862.4 meters which both correspond to the distance between Berlin Central Station and Munich Central Station

Example 2:
Tool output:Yes, there was a significant earthquake in Japan in 2023. The earthquake had a magnitude of around 7.0 and caused considerable damage and disruption.
Expectation:A 7.5 magnitude earthquake struck Japan on Monday afternoon, triggering a tsunami alert and prompting an official warning to residents to evacuate affected coastal areas as soon as possible.
Is correct: false
Reason: The magnitude is wrong 7.5 is expected but got 7.0 which is too big of difference so probably the result is referring to the wrong earthquake.

Example 3:
Tool output:Yes, there are 2 bakeries: John Baker, MOON.
Expectation:Some of the most popular bakeries in Zurich are: John Baker, Emma's Bakery, MOON and Babu's
Is correct: true
Reason: The answer is correct as it is a full subset of the expectation.

Now please evaluate the following tool output and give the reason for your evaluation: '{tool_output}'
{format_instructions}"""
