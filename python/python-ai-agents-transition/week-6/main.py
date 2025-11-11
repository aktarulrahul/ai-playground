# type: ignore
from fastapi import FastAPI

app = FastAPI(title="Week 6 - FastAPI Backend", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Week 6 - FastAPI Backend", "status": "running"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "week": 6} 