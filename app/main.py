from fastapi import FastAPI
from app.api import auth, tasks

app = FastAPI(title="Logika Backend Test")

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def health_check():
    return {"status": "ok"}
