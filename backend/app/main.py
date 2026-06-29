from fastapi import FastAPI
from app.db.database import engine

app = FastAPI(
    title="Tech With Thoufiq API"
)


@app.get("/")
def root():
    return {
        "message": "Database Connected Successfully!"
    }