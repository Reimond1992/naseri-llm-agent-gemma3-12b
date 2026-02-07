# LLM Agent Gemma3:12B – Full Quick Start (FastAPI)

This guide shows how to run the **LLM Agent API** locally using Python and FastAPI.  
The agent uses **Ollama Gemma3:12B** to answer user messages.  

> No Docker is needed – just Python and Ollama.

---

## 🔹 Prerequisites

- **Python 3.12** installed  
  [Python Downloads](https://www.python.org/downloads/)
- **Ollama LLM** installed  
  Make sure **Gemma3:12B** model is downloaded.
- Ollama API must be running on:  
  `http://localhost:11434/api/generate`
- Internet connection to install Python packages

---

## 🔹 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPO_URL>
cd <repo-folder>
🔹 2. Set Up Python Environment
Create a virtual environment:

python -m venv venv
Activate it:

Windows:

venv\Scripts\activate
Linux / Mac:

source venv/bin/activate
🔹 3. Install Dependencies
Make sure you have requirements.txt in the project root, then run:

pip install -r requirements.txt
This will install:

fastapi – the web framework

uvicorn – the server

httpx – for calling Ollama API

pydantic & pydantic-settings – for configuration

🔹 4. Configure Environment Variables
Create a .env file in the project root:

LLM_URL=http://localhost:11434/api/generate
DATABASE_URL=sqlite:///chat.db
TIMEOUT=30
DATABASE_URL points to the SQLite database that stores chat logs.

🔹 5. Run the API
Start the FastAPI server:

uvicorn main:app --host 0.0.0.0 --port 8000 --reload
The API will be available at: http://localhost:8000

Swagger UI for testing: http://localhost:8000/docs

🔹 6. Test the /chat Endpoint
Send a POST request:

POST http://localhost:8000/chat
Content-Type: application/json

{
  "message": "Hello, how are you?"
}
Example JSON response:

{
  "response": "سلام! حال شما چطوره؟"
}
🔹 7. Database
SQLite database file: chat.db (created automatically in project root)

Fields stored per message:

message, response, timestamp, user_id, session_id, intent, response_length, language, processing_time, tool_used

🔹 8. Project Structure
llm-agent-gemma3/
├── main.py
├── core/
│   ├── __init__.py
│   └── config.py
├── db/
│   ├── __init__.py
│   └── chat.db
├── agents/
│   ├── __init__.py
│   └── ollama.py
├── models/
│   ├── __init__.py
│   └── chat.py
├── routers/
│   ├── __init__.py
│   └── chat.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
🔹 9. How It Works
User sends a message to /chat

OllamaAgent analyzes the message (pre-processing)

Sends the processed prompt to Ollama Gemma3:12B

Receives a response and stores both message & response in chat.db

Returns the response to the user

Designed to be easily extendable with Tools, Memory, or multiple LLMs.

🔹 10. Optional Notes
You can change port or host in uvicorn command

Logs are stored in SQLite; you can switch to PostgreSQL if needed

API can be tested using Swagger, Postman, or any HTTP client

Make sure Ollama is running before starting FastAPI

🔹 11. Recommended Usage
Always use a virtual environment for a clean setup

For repeated usage, you can run FastAPI in the background:

uvicorn main:app --host 0.0.0.0 --port 8000
