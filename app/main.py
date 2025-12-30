from fastapi import FastAPI

app = FastAPI(title="Logika Backend Test")

@app.get("/")
def health_check():
    return {"status": "ok"}
