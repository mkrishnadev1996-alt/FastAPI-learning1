# FastAPI Student Management API

A beginner-friendly FastAPI project demonstrating core API concepts through a student management system.

## Overview

This project is a learning-focused FastAPI application that provides a student management system with the following features:

- Retrieve student by ID
- Search student by name
- Get students by class
- Interactive API documentation with Swagger UI

**Learning objectives:** Path parameters, query parameters, Pydantic models, FastAPI enums, and automatic API documentation.

## Prerequisites

- **Python 3.13** (specified in `.python-version`)
- **uv** package manager (modern, fast alternative to pip)

## Installation & Setup

### Step 1: Clone the project

```bash
cd C:\Users\VamsiAD\Dev\FastAPI\learning1
```

### Step 2: Install dependencies

If you don't have `uv` installed:

```bash
pip install uv
```

Install project dependencies:

```bash
uv sync
```

This creates a `.venv` virtual environment with all dependencies.

### Step 3: Activate virtual environment

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Command Prompt)
.venv\Scripts\activate.bat

# Linux/macOS
source .venv/bin/activate
```

## Running the Application

Start the FastAPI server:

```bash
uv run fastapi dev main.py
```

Or use uvicorn directly:

```bash
uv run uvicorn main:app --reload
```

The server starts at `http://127.0.0.1:8000`.

## API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI:** Visit `http://127.0.0.1:8000/docs`
- **ReDoc:** Visit `http://127.0.0.1:8000/redoc`

The `/docs` endpoint provides an interactive interface to test all API endpoints.

## API Endpoints

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| `GET` | `/` | Welcome message with docs link | None |
| `GET` | `/get-student-by-id/{student_id}` | Retrieve student by ID | Path: `student_id` (1-9) |
| `GET` | `/get-student-by-name` | Search student by name | Query: `name` |
| `GET` | `/get-students-in-class/{student_class}` | Get students in a class | Path: `student_class` (1-10) |

### Endpoint Details

#### Root Endpoint

Returns welcome message and documentation link.

```bash
curl http://127.0.0.1:8000/
```

**Response:**
```json
{"message": "Hello world. Refer docs at path /docs"}
```

---

#### Get Student by ID

Fetch a student using their ID (path parameter).

```bash
curl http://127.0.0.1:8000/get-student-by-id/1
```

**Path Parameter:**
- `student_id`: Student ID (must be > 0 and < 10)

**Response (success):**
```json
{"name": "John", "age": 12, "class": 5}
```

**Response (not found):**
```json
{"Error": "Id not found"}
```

---

#### Get Student by Name

Search for a student by name (query parameter).

```bash
curl http://127.0.0.1:8000/get-student-by-name?name=john
```

**Query Parameter:**
- `name`: Student name (case-insensitive search)

**Response (success):**
```json
{"name": "John", "age": 12, "class": 5}
```

**Response (not found):**
```json
{"Error": "Name not found"}
```

---

#### Get Students in Class

Get all students in a specific class.

```bash
curl http://127.0.0.1:8000/get-students-in-class/5
```

**Path Parameter:**
- `student_class`: Class number (1-10)

**Response (success):**
```json
{"class": 5, "data": [{"name": "John", "age": 12, "class": 5}, {"name": "Ken", "age": 12, "class": 5}]}
```

**Response (no students):**
```json
{"Error": "No students found in this class"}
```

## Project Structure

```
learning1/
├── main.py          # FastAPI application (66 lines)
├── pyproject.toml   # Project configuration
├── requirements.txt # Dependencies
├── README.md        # This file
└── .venv/           # Virtual environment
```

### main.py Overview

- **Imports:** FastAPI, Path, Query, BaseModel, Field, Enum
- **Data models:** `InputModel` (Pydantic), `StudentClass` (Enum)
- **Student data:** In-memory dictionary with 4 sample students
- **Endpoints:** 4 routes demonstrating different parameter types

## Learning Takeaways

This project demonstrates core FastAPI concepts:

1. **Path Parameters:** Strongly typed URL parameters with validation (`Path(..., gt=0, lt=10)`)
2. **Query Parameters:** Optional/required query string parameters (`Query(...)`)
3. **Pydantic Models:** Data validation using `BaseModel` and `Field`
4. **Enums:** Type-safe enum handling for constrained values
5. **Automatic Docs:** Swagger UI and ReDoc generation
6. **Error Handling:** Graceful error responses for missing data
7. **FastAPI Decorators:** `@app.get()` for route definition

## Example Use Cases

- Build a simple student management system
- Learn FastAPI fundamentals before moving to complex projects
- Template for CRUD API development
- Reference for parameter validation patterns

## Dependencies

- `fastapi[standard]>=0.136.1` - Web framework
- `uvicorn>=0.46.0` - ASGI server

## License

This project is for educational purposes.
