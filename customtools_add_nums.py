from langchain_core.tools import tool

@tool 
def add(num1: int, num2:int):
    return num1 + num2


result = add.invoke({"num1" : 12, "num2" : 23 })
print(result)

