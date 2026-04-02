# Candidate Management API

Backend API built with FastAPI for managing candidates in a recruitment system.

## Assignment Coverage

This project implements all required features:

1. Create Candidate: `POST /candidates`
2. Get All Candidates: `GET /candidates`
3. Optional status filter: `GET /candidates?status=interview`
4. Update Candidate Status: `PUT /candidates/{id}/status`

Validation included:

- `email` must be valid
- `status` must be one of: `applied`, `interview`, `selected`, `rejected`

## Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest

## Project Structure

```text
.
|-- app/
|   |-- __init__.py
|   |-- database.py
|   |-- main.py
|   |-- models.py
|   `-- schemas.py
|-- tests/
|   `-- test_api.py
|-- requirements.txt
`-- README.md
```

## Setup

1. Create a virtual environment:

```powershell
python -m venv .venv
```

2. Activate virtual environment (Windows PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Run the API

```powershell
python -m uvicorn app.main:app --reload
```

API will be available at:

- `http://127.0.0.1:8000`
- Swagger docs: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Endpoints

### 1) Create Candidate

`POST /candidates`

Request body:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "skill": "Python",
  "status": "applied"
}
```

### 2) Get All Candidates

`GET /candidates`

Optional filter:

`GET /candidates?status=interview`

### 3) Update Candidate Status

`PUT /candidates/{id}/status`

Request body:

```json
{
  "status": "interview"
}
```

## Run Tests

```powershell
python -m pytest -q
```

## Deploy on Render (Free)

Use these values when creating the Web Service:

- Runtime: Python
- Build Command: python -m pip install -r requirements.txt
- Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT

This repo includes [runtime.txt](runtime.txt) to use a stable Python version on Render.

## Notes

- Data is persisted in SQLite.
- Duplicate candidate emails are rejected with a clear error response.

AUTHOR: Jay Joshi

Email: joshijayy421@gmail.com

LinkedIn: https://www.linkedin.com/in/jay-joshi-75b75124b/

GitHub: https://github.com/jayyx3

Portfolio: https://jay-portfolio-ten-tawny.vercel.app/