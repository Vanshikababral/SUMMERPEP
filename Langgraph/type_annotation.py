from typing import TypedDict

class Student(TypedDict):
    name : str
    year : int

stu = Student(
    name = "Vanshika", 
    year = "2005"
)

print(stu)
print(type(stu))