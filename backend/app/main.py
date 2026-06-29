from fastapi import FastAPI

app = FastAPI(
    title="Tech With Thoufiq API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Tech With Thoufiq API 🚀"
    }