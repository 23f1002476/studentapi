from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

students = []

# Read CSV
with open("q-fastapi.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        students.append(
            {
                "studentId": int(row["studentId"]),
                "class": row["class"]
            }
        )


@app.get("/api")
async def get_students(
    class_: list[str] | None = Query(default=None, alias="class")
):
    if class_:
        filtered = [
            student
            for student in students
            if student["class"] in class_
        ]
        return {"students": filtered}

    return {"students": students}