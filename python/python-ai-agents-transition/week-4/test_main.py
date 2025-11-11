# type: ignore
import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_root():
    """Test the root endpoint"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Week 4 - FastAPI Backend"
        assert data["status"] == "running"

@pytest.mark.asyncio
async def test_health():
    """Test the health endpoint"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["week"] == 4 