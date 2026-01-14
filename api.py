from fastapi import FastAPI
from pydantic import BaseModel

@app.get("/")
def home():
    return {"message": "Bird Cloud API is running. Use /detections and /add endpoints."}

app = FastAPI()
storage = []

class Detection(BaseModel):
    time: str
    species: str
    confidence: float

@app.post("/add")
def add_detection(d: Detection):
    storage.append(d)
    return {"status": "ok"}

@app.get("/detections")
def get_detections():
    return storage[-200:]
