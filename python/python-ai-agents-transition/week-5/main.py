# type: ignore
from fastapi import FastAPI

app = FastAPI(title="Week 5 - FastAPI Backend", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Week 5 - FastAPI Backend", "status": "running"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "week": 5} 