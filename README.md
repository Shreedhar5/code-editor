# Online Code Editor with Interactive Terminal

## Overview

This is a beginner-friendly online coding editor designed especially for young learners to write, run, and see the output of their code easily. It supports **Python execution with input**, as well as live previews for **HTML, CSS, and JavaScript** code.

The project features a simple, clean UI focused on ease of use for kids and learners.

---

## Features

* **Toggleable Light/Dark Theme:** Easily switch between themes for comfortable coding.
* **Code Load & Download:** Save your current code or load saved files.
* **Multi-language Support:**

  * Python code execution with support for user input.
  * Live rendering of HTML, CSS, and JavaScript with instant preview.
* **Dedicated Input Box:** Separate input area for feeding input to Python programs.
* **Output Display:** Terminal-style output for Python programs; live web preview for HTML/CSS/JS.
* **User-Friendly Interface:** Designed to be intuitive and accessible for young coders.
* **Secure Execution:** Code runs in a Docker container backend for safe isolation.

---

## How It Works

* Frontend uses a code editor component for syntax highlighting and editing.
* Users write code and enter optional inputs in the input box.
* On Run, the frontend sends code, input, and language choice to the Flask backend API.
* Backend executes Python code inside a temporary file with user input piped to stdin.
* For web languages, backend returns combined HTML/CSS/JS as a live preview.
* Output or rendered content is displayed immediately on frontend.
* Includes timeout and error handling for stable operation.

---

## Project Structure

```
TP/
│
├── app.py             # Flask backend application
├── Dockerfile         # Dockerfile to containerize the app
├── requirements.txt   # Python dependencies
├── templates/         # HTML templates folder
│   └── index.html     # Main frontend UI template
├── Procfile           # For deployment (e.g. Railway)
```

---

## Setup & Run Locally

1. Clone the repo and navigate into `TP` directory.

2. Build the Docker image:

   ```
   docker build -t online-code-editor .
   ```

3. Run the container:

   ```
   docker run -p 5000:5000 online-code-editor
   ```

4. Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## Deployment

* Ready for deployment on platforms like Railway, Heroku, or any Docker-compatible cloud provider.

* Use this Procfile:

  ```
  web: python app.py
  ```

* The app listens on the port provided by the environment variable `PORT`.

---

## Tech Stack

* **Frontend:** HTML, CSS, JavaScript, CodeMirror/Monaco (for syntax highlighting)
* **Backend:** Python Flask API
* **Execution:** Runs user Python code inside Docker container for safety
* **Deployment:** Designed for containerized cloud deployment (Railway, Heroku, etc.)

---




