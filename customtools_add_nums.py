from langchain_core.tools import tool

@tool 
def add(num1: int, num2:int)->int:
    """Adds two integers and returns the sum."""
    return num1 + num2

@tool
def weather_of_Jalandhar(text:str)->int:
    """This return the current temperatre of City"""
    return 36


result = weather_of_Jalandhar.invoke({"text": "Jalandhar"})
print(result)

