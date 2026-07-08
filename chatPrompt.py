import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
load_dotenv()
llm = ChatAnthropic(
    model="claude-sonnet-5",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)
st.header("This is Chatbot for implementation Multi- Msg")

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant specialized in {domain}."),
    ("human", "{topic}")
])

prompt_value = chat_prompt.invoke({
    "domain": "Healthcare",
    "topic": "AI in Healthcare"
})

if st.button("Generate"):

    prompt = chat_prompt.invoke({
        "domain": "Healthcare",
        "topic": "Explain AI in Healthcare."
    })

    response = llm.invoke(prompt)

    result = parser.invoke(response)

    st.write(result)