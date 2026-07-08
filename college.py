#Prompts
import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(
    model="claude-sonnet-5",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

prompt = input("Ask your question: ")

response = llm.invoke(prompt)

print(response.content)







#Printing no of lines by selecting from a dropdown and using the same PromptTemplate and OutputParser
#import os
# from dotenv import load_dotenv
# from langchain_anthropic import ChatAnthropic
# import streamlit as st
# from langchain_core.messages import SystemMessage, HumanMessage
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import PromptTemplate
# load_dotenv()

# parser = StrOutputParser()

# llm = ChatAnthropic(
#     model="claude-sonnet-5",
#     api_key=os.getenv("ANTHROPIC_API_KEY")
# )

# st.header("College Research Assistant")

# info_type = st.selectbox(
#     "How many lines do you want to generate about the college?",
#     [
#         "1",
#         "2",
#         "3",
#         "4",
#         "5",
#         "6",
#         "7",
#         "8",
#         "9",
#         "10"
#     ]
# )

# college_name = st.text_input("Enter college name: ")

# if st.button("Submit"):
#     prompt_template = PromptTemplate(
#         input_variables=["college_name", "info_type"],
#         template="""
#         You are a College Research Assistant.
#         Generate exactly {info_type} concise points about the college '{college_name}'.
#         Keep the tone polite and informative.
#     """
#     )
#     system_prompt = prompt_template.format(
#         college_name=college_name,
#         info_type=info_type
#     )
#     response = llm.invoke([
#         SystemMessage(content=system_prompt),
#         HumanMessage(content=f"Tell me about {college_name}.")
#     ])

#     result = parser.invoke(response)

#     st.subheader(f"{info_type} of {college_name}")
#     st.write(result)

