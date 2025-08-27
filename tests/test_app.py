import sys
import os
import pytest
from httpx import AsyncClient

# Add project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.mark.asyncio
async def test_read_main():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "<h1>Eliminador de Marcas de Agua de Gamma.ai</h1>" in response.text