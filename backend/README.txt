Library Management Backend
==========================

Prerequisites
-------------

- Python 3.11 or later
- PostgreSQL

Installation (Windows PowerShell)
----------------------------------

From the `backend` directory:

    py -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    pip install -r requirements.txt

Create a `.env` file in the `backend` directory. Set the database connection
and JWT settings, for example:

    DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/library_management
    JWT_SECRET_KEY=replace-with-a-long-random-secret
    JWT_ALGORITHM=HS256
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30

Running the application
-----------------------

From the `backend\app` directory, with the virtual environment activated:

    uvicorn main:app --reload

The API is available at http://127.0.0.1:8000.
Interactive API documentation is available at:

    http://127.0.0.1:8000/docs