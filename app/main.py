import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    # will be set in container/release later
    return {"version": os.getenv("APP_VERSION", "dev")}
