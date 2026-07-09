from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []

class Student(BaseModel):
    name: str
    age: int
    grade: str

@app.post("/students")
def create_student(student: Student):
    students.append(student.model_dump())
    return {
        "message": "Student created successfully",
        "student": student
    }

@app.get("/students_data")
def get_students():
    return {
        "students": students
    }

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id >= len(students):
        return {"message": "Student not found"}

    students[student_id] = student.model_dump()

    return {
        "message": "Student updated successfully",
        "student": students[student_id]
    }

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id >= len(students):
        return {"message": "Student not found"}

    deleted_student = students.pop(student_id)

    return {
        "message": "Student deleted successfully",
        "student": deleted_student
    }
