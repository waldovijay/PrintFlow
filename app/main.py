from fastapi import FastAPI
from app.database import create_db

app = FastAPI(title="PrintFlow")

@app.on_event("startup")
def startup():
    create_db()

@app.get("/")
def home():
    return {"application":"PrintFlow","version":"0.1"}
