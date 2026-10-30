
from fastapi import FastAPI
from db.database import engine, Base

from models.user import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "User API is running"}
