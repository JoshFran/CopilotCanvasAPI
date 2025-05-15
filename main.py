from fastapi import FastAPI
from pydantic import BaseModel
import os
from canvasapi import Canvas

API_URL = "https://webcourses.ucf.edu"
TOKEN = os.getenv("CANVAS_TOKEN")

app = FastAPI()

class CourseRequest(BaseModel):
    courseId: int

@app.get("/")
def root():
    return "Canvas Assignment API is running."

@app.get("/getAssignments")
def get_assignments(courseId: int):
    canvas = Canvas(API_URL, TOKEN)
    course = canvas.get_course(courseId)
    assignments = course.get_assignments()

    assignment_names = [a.name for a in assignments]
    
    if not assignment_names:
        return "There are no assignments in this course."

    return f"There are {len(assignment_names)} assignments: " + ", ".join(assignment_names)
