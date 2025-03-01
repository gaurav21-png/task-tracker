# Here's the updated code with all the fixes applied.
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task Tracker")


class Task(BaseModel):
    id: int
    title: str
    done: bool = False


tasks: dict[int, Task] = {}


@app.post("/tasks", status_code=201)
def create_task(task: Task) -> Task:
    if task.id in tasks:
        raise HTTPException(status_code=409, detail="Task already exists")
    tasks[task.id] = task
    return task


@app.get("/tasks/{task_id}")
def get_task(task_id: int) -> Task:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]


@app.patch("/tasks/{task_id}/done")
def complete_task(task_id: int) -> Task:
    task = get_task(task_id)
    task.done = True
    return task
