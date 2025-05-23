from fastapi import FastAPI
from pydantic import BaseModel
import os
from canvasapi import Canvas

API_URL = "https://webcourses.ucf.edu"
TOKEN = os.getenv("CANVAS_TOKEN")

app = FastAPI()

class CourseRequest(BaseModel):
    courseId: int

@app.post("/getFiles")
def get_files(req: CourseRequest):
    print("Received request for courseId:", req.courseId)
    canvas = Canvas(API_URL, TOKEN)
    course = canvas.get_course(req.courseId)
    course_files = course.get_files()
    print("Retrieved files:", course_files)

    files = [
        {"id": f.id, "display_name": f.display_name, "url": f.url}
        for f in course_files
    ]
    return {"fileCount": len(files), "files": files}

