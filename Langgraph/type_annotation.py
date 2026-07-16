from typing import TypedDict, List

class Student(TypedDict):
    name : str
    year : int
    marks : List[int]

stu = Student(
    name = "Vanshika", 
    year = "2005",
    marks = [21 , 23, 24, 25]
)

print(stu)
print(type(stu))