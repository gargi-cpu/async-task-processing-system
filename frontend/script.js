const API_URL = "http://127.0.0.1:8000";

async function createTask() {
  const taskName = document.getElementById("taskInput").value;

  const response = await fetch(`${API_URL}/tasks?task_name=${taskName}`, {
    method: "POST"
  });

  const data = await response.json();

  document.getElementById("taskId").innerText =
    "Task ID: " + data.task_id;

  checkStatus(data.task_id);
}

function checkStatus(taskId) {
  const interval = setInterval(async () => {
    const res = await fetch(`${API_URL}/tasks/${taskId}`);
    const data = await res.json();

    document.getElementById("taskStatus").innerText =
      "Status: " + data.status;

    if (data.status === "COMPLETED") {
      clearInterval(interval);
    }
  }, 1000);
}
