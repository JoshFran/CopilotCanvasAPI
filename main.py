from fastapi import FastAPI, Query
from canvasapi import Canvas
import os

API_URL = "https://webcourses.ucf.edu"
TOKEN = os.getenv("CANVAS_TOKEN")

app = FastAPI()

@app.get("/getFiles")
def get_files(courseId: int = Query(...)):
    canvas = Canvas(API_URL, TOKEN)
    course = canvas.get_course(courseId)
    
    files = [
        {"id": f.id, "display_name": f.display_name, "url": f.url}
        for f in course.get_files()
    ]

    return {"fileCount": len(files), "files": files}
