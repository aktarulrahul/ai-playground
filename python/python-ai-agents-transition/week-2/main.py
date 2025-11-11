# type: ignore
import httpx
from fastapi import FastAPI, Depends, HTTPException
from schemas import Tea, TeaCreate
from db import database, teas
from deps import get_db

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

@app.get("/health")
async def health_check():
    """Health check endpoint for Docker"""
    return {"status": "healthy", "timestamp": "2024-01-01T00:00:00Z"}

@app.post("/teas/", response_model=Tea)
async def create_tea(tea: TeaCreate, db=Depends(get_db)):
    query = teas.insert().values(name=tea.name, description=tea.description)
    last_record_id = await db.execute(query)
    return {**tea.dict(), "id": last_record_id}

@app.get("/teas/", response_model=list[Tea])
async def list_teas(db=Depends(get_db)):
    query = teas.select()
    return await db.fetch_all(query)

@app.get("/teas/{tea_id}", response_model=Tea)
async def get_tea(tea_id: int, db=Depends(get_db)):
    query = teas.select().where(teas.c.id == tea_id)
    tea = await db.fetch_one(query)
    if tea is None:
        raise HTTPException(status_code=404, detail="Tea not found")
    return tea

@app.delete("/teas/{tea_id}", response_model=Tea)
async def delete_tea(tea_id: int, db=Depends(get_db)):
    query = teas.select().where(teas.c.id == tea_id)
    tea = await db.fetch_one(query)
    if tea is None:
        raise HTTPException(status_code=404, detail="Tea not found")
    delete_query = teas.delete().where(teas.c.id == tea_id)
    await db.execute(delete_query)
    return tea

@app.get("/fastapi-docs")
async def docs_redirect():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://fastapi.tiangolo.com/")
        return response.text


