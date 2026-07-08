import os
from dotenv import load_dotenv
import streamlit as st

from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatAnthropic(
    model="claude-sonnet-5",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

parser = StrOutputParser()

st.header("College Research Assistant")

info_type = st.selectbox(
    "What would you like to know?",
    [
        "Overview",
        "Admissions",
        "Courses",
        "Fees",
        "Placements",
        "Scholarships",
        "Campus Life"
    ]
)

college_name = st.text_input("Enter College Name")

if st.button("Submit"):

    prompt = PromptTemplate(
        input_variables=["college_name", "info_type"],
        template="""
You are a College Research Assistant.

Generate exactly 5 concise points about the {info_type} of {college_name}.

Keep the response polite and informative.
"""
    )

    chain = prompt | llm | parser

    result = chain.invoke({
        "college_name": college_name,
        "info_type": info_type
    })

    st.subheader(f"{info_type} of {college_name}")
    st.write(result)