import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import RunnableParallel
from langchain_core.prompts import PromptTemplate
load_dotenv()

city = input("Enter the city name: ")

prompt1 = PromptTemplate.from_template("You are a travel planner.Help me find tourist attracion spot of {city}.")

prompt2 = PromptTemplate.from_template("You are a travel planner. Help me find the best food courts in the {city}.")

prompt3 = PromptTemplate.from_template("You are a travel planner. Help me deciding the best time to visit {city}.")

model1 = ChatOpenAI(
    model="gpt-5.5",
    api_key=os.getenv("OPENAI_API_KEY")
)

model2 = ChatAnthropic(
    model = "claude-sonnet-5",
    api_key = os.getenv("ANTHROPIC_API_KEY")
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    chain1 = prompt1 | model1 | parser,
    chain2 = prompt2 | model2 | parser,
    chain3 = prompt3 | model1 | parser
)

result = parallel_chain.invoke(
    {"city" : city}
)

print(result["chain1"])
print(result["chain2"])
print(result["chain3"])
