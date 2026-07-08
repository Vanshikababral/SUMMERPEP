import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic
load_dotenv()

no_of_jokes = input("Enter the number of jokes: ")
topic = input("Enter the joke topic: ")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a joke generator that creates {no_of_jokes} jokes about {topic}.")
    ]
)
prompt1 = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant and an expert joke generator."),
        (
            "human", "Analyze the following joke(s):{response}Create a better and funnier version.Return the response in the following format:"
            "Old Joke:"
            "Analysis:"
            "New Joke:")
    ]
)

model = ChatOpenAI(
    model ="gpt-5.5",
    api_key =os.getenv("OPENAI_API_KEY")
)

model1 = ChatAnthropic(
    model="claude-sonnet-5",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)
parser = StrOutputParser()

chain = prompt | model | parser
chain1 = prompt1 | model1 | parser

result = chain.invoke(
    {
        "no_of_jokes": no_of_jokes,
        "topic": topic
    }
)
final_result = chain1.invoke(
    {
        "response": result
    }
)

print(result)
print(final_result)
chain.get_graph().print_ascii()