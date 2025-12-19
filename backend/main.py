from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import threading
import time
import uuid

# ✅ THIS LINE WAS MISSING
app = FastAPI(title="Async Task Processing System")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory task store
tasks = {}

def process_task(task_id: str):
    tasks[task_id]["status"] = "PROCESSING"
    time.sleep(5)  # simulate heavy work
    tasks[task_id]["status"] = "COMPLETED"
    tasks[task_id]["result"] = "Task completed successfully"

@app.post("/tasks")
def create_task(task_name: str):
    task_id = str(uuid.uuid4())
    tasks[task_id] = {
        "task_name": task_name,
        "status": "PENDING",
        "result": None
    }
    thread = threading.Thread(target=process_task, args=(task_id,))
    thread.start()
    return {"task_id": task_id}

@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    return tasks.get(task_id, {"error": "Task not found"})
