from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
# model=ChatOpenAI(api_key=apik, model_name="gpt-4o-mini-2024-07-18", temperature=0.7)
model=ChatGoogleGenerativeAI(api_key=gemapi, model="gemini-2.5-flash", temperature=0.7)
promt1 = input("Enter what you want to ask: ");
result1= model.invoke(promt1)
promt2 = input("Enter what you want to ask: ");
result2= model.invoke(promt2)
print("Result 1:", result1.content)
print("Result 2:", result2.content)
