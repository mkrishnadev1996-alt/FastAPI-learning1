from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from enum import Enum

app =FastAPI()

# Model for adding new student
class AddStudent(BaseModel):
    name:str = Field(...,description="Name of the student")
    age:int = Field(...,description="Age of the student", ge=5, le=18)
    student_class:int = Field(...,description="Class of the student",ge=1,le=10)



class StudentClass(int ,Enum):
    one = 1,
    two = 2,
    three = 3,
    four = 4,
    five = 5,
    six = 6,
    seven = 7,
    eight = 8,
    nine = 9,
    ten = 10



students ={
    1:{"name":"John",
       "age":12,
       "class":5},
    2:{"name":"Missy",
       "age":10,
       "class":3},
    3:{"name":"Sara",
       "age":13,
       "class":6},
    4:{"name":"Ken",
       "age":12,
       "class":5},
}

@app.get("/")
def index():
    return {'message':'Hello world. Refer docs at path /docs'}

@app.get("/get-student-by-id/{student_id}")
async def get_student_by_id(student_id: int = Path(..., description="Enter Id of student", gt=0, lt=10)):
    if student_id not in students:
        return {"Error":"Id not found"}
    return students[student_id]

@app.get("/get-student-by-name")
async def get_student_by_name(name : str = Query(...,description="Name of the student")):
    for id in students.keys():
        if students[id]["name"].lower()==name.lower() :
            return students[id]
    return {"Error":"Name not found"}

@app.get("/get-students-in-class/{student_class}")
async def get_students_in_class(student_class :StudentClass = Path(...,description="Class for which list of students are required")):
    result = []

    for student in students.values():
        if student["class"] == student_class.value:
            result.append(student)

    if not result:
        return {"Error": "No students found in this class"}

    return {"class":student_class,"data":result}

@app.post("/add-student")
async def add_student(student: AddStudent):
    if student:
        try:
            id = max(students.keys()) + 1
            students[id] = student.model_dump()
            return {"Message":"Student is added"}
        except Exception as e:
            print(e)
            return {"Error": e}
