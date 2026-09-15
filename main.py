from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Student Management API",
    description="A simple REST API for managing students",
    version="1.0.0",
)


class Student(BaseModel):
    name: str
    age: int
    course: str


students = []
next_id = 1


@app.get("/")
def root():
    return {"message": "Student Management API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/students")
def create_student(student: Student):
    global next_id

    new_student = {
        "id": next_id,
        "name": student.name,
        "age": student.age,
        "course": student.course,
    }

    students.append(new_student)
    next_id += 1

    return new_student


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(status=404, detail="Student not found")


@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for student in students:
        if student["id"] == student_id:
            student["name"] = updated_student.name
            student["age"] = updated_student.age
            student["course"] = updated_student.course

            return student

    raise HTTPException(status_code=404, detail="Student not found")


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {"message": "Student deleted successfully"}

    raise HTTPException(status_code=404, detail="Student not found")
