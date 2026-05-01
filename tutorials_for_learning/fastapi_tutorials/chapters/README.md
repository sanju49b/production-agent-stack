# FastAPI Tutorial Series

A hands-on, notebook-based course for learning FastAPI from the ground up. Each chapter covers a specific topic with working code examples you can run directly in Jupyter.

---

## Prerequisites

- Python 3.10+
- Basic Python knowledge (functions, classes, type hints)
- No prior FastAPI or async experience needed

Install the required packages:

```bash
pip install fastapi[all] sqlalchemy psycopg2 python-jose[cryptography] passlib[bcrypt]
```

---

## Chapter Overview

### Chapter 1 — FastAPI Fundamentals (`Fastapi_1.ipynb`)
The biggest notebook in the series. Covers the core building blocks of FastAPI:
- Creating a FastAPI app and running it with Uvicorn
- HTTP methods: GET, POST, PUT, DELETE
- Path parameters and query parameters
- Request body with Pydantic models
- Response models and status codes
- Auto-generated interactive docs (Swagger UI at `/docs`)

**Start here if you are brand new to FastAPI.**

---

### Chapter 2 — Building APIs (`Fastapi_2.ipynb`)
Focuses on the fundamentals of designing real API routes:
- Defining routes with HTTP method decorators (`@app.get`, `@app.post`, etc.)
- Path parameters to identify specific resources (e.g. `/items/42`)
- Query parameters for filtering and pagination (e.g. `/items/?skip=5&limit=20`)
- Combining path and query parameters in a single route

---

### Chapter 3 — Data Validation Part 1 (`data_validation_part1.ipynb`)
Covers how Pydantic keeps your data clean:
- Defining a `BaseModel` with required and optional fields
- Automatic request validation — FastAPI rejects bad data before it hits your logic
- Custom validators with `@validator` / `@field_validator`
- `Field()` constraints: `min_length`, `ge` (greater-than-or-equal), `le`, regex patterns

---

### Chapter 4 — Data Validation Part 2 (`data_validation_part2.ipynb`)
Continues where Part 1 left off with more advanced validation patterns.

---

### Chapter 5 — Async Programming (`async_part1.ipynb`)
Explains why and how to write non-blocking FastAPI endpoints:
- Synchronous vs asynchronous code — why blocking I/O hurts throughput
- `async def` and `await` — the two keywords you need
- Simulating concurrent I/O (database queries, external API calls)
- Practical example: fetching user data and transaction history concurrently so two 1-second tasks take ~1 second total instead of 2

---

### Chapter 6 — Databases (`databases_part1.ipynb`)
Connecting FastAPI to a real database with SQLAlchemy ORM:
- Choosing a database URL (SQLite for dev, PostgreSQL for production)
- `create_engine` — the bridge between Python and the database
- Defining ORM models (Python classes → database tables)
- `Base.metadata.create_all()` — safely creating tables on startup
- Sessions and dependency injection for database access
- Full CRUD API: Create, Read, Update, Delete

---

### Chapter 7 — Authentication Basics (`basics_Authentication.ipynb`)
Introduces user authentication concepts:
- Password hashing with `passlib`
- Creating and verifying JWT tokens with `python-jose`
- Protecting routes with OAuth2 password flow
- `Depends()` for injecting the current authenticated user

---

### Chapter 8 — Security & Authentication (`security_and_Authentication.ipynb` + `authentication_security.ipynb`)
Deeper dive into securing a FastAPI application:
- OAuth2 with Bearer tokens end-to-end
- Token expiry and refresh patterns
- Role-based access control concepts
- Security best practices

---

### Hands-on Project — API Design (`api_design/`)

A structured project that puts everything together. Use this after completing the notebooks to see how a real FastAPI codebase is organized.

```
api_design/
├── app/
│   ├── main.py       # FastAPI app entry point, registers routers
│   ├── schema.py     # Pydantic request/response models
│   └── crud.py       # Database operations (Create, Read, Update, Delete)
├── api/
│   ├── product.py    # /products routes
│   └── user.py       # /users routes
├── core/
│   ├── config.py     # App settings (loaded from environment variables)
│   └── security.py   # Password hashing, JWT helpers
├── db/               # Database connection and session setup
└── tests/
    ├── test_products.py
    └── test_users.py
```

Run the app:

```bash
cd api_design
uvicorn app.main:app --reload
```

Then open `http://127.0.0.1:8000/docs` to explore the interactive API.

Run tests:

```bash
pytest tests/
```

---

## Recommended Learning Path

```
Fastapi_1.ipynb
    ↓
Fastapi_2.ipynb
    ↓
data_validation_part1.ipynb → data_validation_part2.ipynb
    ↓
async_part1.ipynb
    ↓
databases_part1.ipynb
    ↓
basics_Authentication.ipynb → security_and_Authentication.ipynb → authentication_security.ipynb
    ↓
api_design/  (capstone project)
```

---

## Quick Reference

| Concept | Notebook | Key Tool |
|---|---|---|
| HTTP routes | `Fastapi_1`, `Fastapi_2` | `@app.get/post/put/delete` |
| Request validation | `data_validation_part1` | `pydantic.BaseModel` |
| Field constraints | `data_validation_part1` | `pydantic.Field` |
| Non-blocking I/O | `async_part1` | `async def` / `await` |
| Database ORM | `databases_part1` | `SQLAlchemy` |
| Auth tokens | `basics_Authentication` | `python-jose`, `passlib` |
| Full project layout | `api_design/` | all of the above |
