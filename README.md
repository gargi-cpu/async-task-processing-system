---

## 🧩 Problem Statement

In real-world applications, many operations take time to complete — such as data processing, AI inference, report generation, or background jobs.  
If these tasks are handled synchronously, the server blocks the request and forces the user to wait, leading to poor performance and bad user experience.

**The challenge:**  
How can we process long-running tasks **without blocking the user** while still allowing them to track progress?

---

## 💡 Solution Overview

This project implements an **Asynchronous Task Processing System** that decouples task execution from user interaction.

Instead of making the user wait:
- The backend accepts the task request
- Immediately returns a unique task ID
- Processes the task in the background
- Allows the client to poll task status using APIs

This mirrors how real production systems handle background jobs.

---

## 🧠 Design Approach & Thinking

The core design principle is:

> **“Never block the user for long-running operations.”**

### Key ideas applied:
- Asynchronous execution using background threads
- Task lifecycle management (PENDING → COMPLETED)
- REST API–based communication
- Frontend polling for real-time updates
- Clear separation between frontend and backend

This approach reflects industry-standard backend architecture patterns.

---

## ⚙️ System Workflow

### Step 1: Task Creation (Frontend)
- User enters a task name
- Clicks **Create Task**
- Frontend sends a POST request to backend

### Step 2: Task Registration (Backend)
- Backend generates a unique UUID for the task
- Stores task details with status `PENDING`
- Starts processing the task asynchronously
- Immediately returns the task ID

### Step 3: Background Processing
- Task runs in a separate thread
- Simulates long-running computation
- Updates task status to `COMPLETED` once finished

### Step 4: Status Tracking (Frontend)
- Frontend periodically polls backend using task ID
- Displays live task status to the user

---

## 🏗 Architecture Diagram (Conceptual)


