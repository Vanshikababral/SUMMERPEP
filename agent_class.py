from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.agents import create_tool_calling_agent
from langchain_classic.agents import AgentExecutor


# Tool 1
@tool
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b


# Tool 2
@tool
def weather_jalandhar() -> str:
    """Returns the current temperature in Jalandhar."""
    return "The current temperature in Jalandhar is 36°C."

# Create LLM
llm = ChatOpenAI(
    model="gpt-4.1",
    temperature=0
)

# Create Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])


# Create Agent
tools = [add_numbers, weather_jalandhar]

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

# Create Agent Executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

# Example : Addition
response = agent_executor.invoke({
    "input": "Add 25 and 35."
})

print("\nAddition Output")
print(response["output"])
