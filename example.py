# #MODEL USING OPENAI API
# import os
# from openai import OpenAI


# client = OpenAI()

# response = client.responses.create(
#     model="gpt-5.4-mini",
#     input="Write a one-sentence bedtime story about a unicorn."
# )

# print(response.output_text)


# #MODEL USING LANGCHAIN
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-5.4-mini",
    #max_completion_tokens=100,
    temperature=0 #deterministic -- use btw 0.5 to 1.5
)

prompt = "Tell me about avengers" 
result = model.invoke(prompt)
print(result.content)


#USED GEMINI API - GEMINI MODEL USING LANGCHAIN
# import os
# from langchain_google_genai import ChatGoogleGenerativeAI


# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
# response = model.invoke("Why do parrots talk?")
# print(response.content)