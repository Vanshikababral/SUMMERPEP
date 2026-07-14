import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

llm = ChatOpenAI(
    model="gpt-5.5",
    temperature=0
)

search_tool = TavilySearch(max_results=2)

#Binding Tools 
llm_with_tools = llm.bind_tools([search_tool])

#Calling Tools 
response = llm_with_tools.invoke(
    "What are today's latest technology news headlines?"
)

print("Tool Calls:")
print(response.tool_calls)

#Executing Tools 
if response.tool_calls:
    tool_call = response.tool_calls[0]

    result = search_tool.invoke(tool_call["args"])

    print("\nSearch Result:")
    print(result)
else:
    print("\nLLM Response:")
    print(response.content)



# import os
# from dotenv import load_dotenv
# import streamlit as st

# from langchain_openai import ChatOpenAI
# from langchain_tavily import TavilySearch

# load_dotenv()

# # Create LLM
# llm = ChatOpenAI(
#     model="gpt-5.5",
#     temperature=0
# )

# # Create Tavily Tool
# search_tool = TavilySearch(max_results=3)

# # Bind Tool
# llm_with_tools = llm.bind_tools([search_tool])

# # ---------------- Streamlit UI ----------------

# st.title("📰 AI News Assistant")

# query = st.text_input(
#     "Enter your news query:",
#     placeholder="e.g. Today's latest AI news"
# )

# if st.button("Search"):

#     if query.strip() == "":
#         st.warning("Please enter a query.")
#     else:

#         response = llm_with_tools.invoke(query)

#         if response.tool_calls:

#             tool_call = response.tool_calls[0]

#             result = search_tool.invoke(tool_call["args"])

#             st.subheader("Search Results")

#             st.write(result)

#         else:
#             st.subheader("LLM Response")
#             st.write(response.content)