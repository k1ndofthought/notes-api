# Simple Notes API 📝

A minimal REST API built with **FastAPI** for creating, reading, and deleting notes.
Data is stored in a **SQLite database** using **SQLAlchemy**.

This project was built to learn real-world API fundamentals:
- REST structure
- Request/response flow
- Database persistence
- Frontend ↔ Backend communication

---

## Tech Stack
- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- HTML, CSS, JavaScript (simple frontend)

---

## Features
- Create a note
- List all notes
- Delete a note
- Automatic API docs with Swagger UI

---

## Project Structure
```
simple-notes-api/
│
├── main.py # FastAPI app & routes
├── models.py # Database models
├── database.py # DB connection & session
├── frontend/ # Simple HTML/JS frontend
├── notes.db # SQLite database (generated)
└── README.md
```

---

## How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/k1ndofthought/notes-api.git
cd notes-api
```
### 2. Create virtual environment
```bash
python -m venv venv
```
### 3. Activate it

for Windows
```bash
venv\Scripts\activate
```

for Mac/Linux
```bash
source venv/bin/activate
```
### 4. Install dependencies
```bash
pip install fastapi uvicorn sqlalchemy
```
### 5. Run the server
```bash
uvicorn main:app --reload
```
## API Docs

### Open in your browser:
```bash
 http://127.0.0.1:8000/docs
```
### Why this project exists?

This is a learning project focused on clarity and fundamentals, not over-engineering.
It serves as a base for future extensions like:
- Authentication
- User accounts
- Deployment


---
