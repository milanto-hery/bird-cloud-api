from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app
app = FastAPI(title="Bird Cloud API")

# Enable CORS so your dashboard can read from anywhere
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for detections
storage = []

# Define the data model for POST /add
class Detection(BaseModel):
    time: str
    species: str
    confidence: float

# Friendly home page
@app.get("/")
def home():
    return {
        "message": "Bird Cloud API is running. Use /detections (GET) and /add (POST) endpoints."
    }

# POST endpoint to add a new detection
@app.post("/add")
def add_detection(d: Detection):
    storage.append(d.dict())  # store as dictionary
    return {"status": "ok", "stored": d.dict()}

# GET endpoint to retrieve latest detections
@app.get("/detections")
def get_detections():
    # Return last 200 detections
    return storage[-200:]
