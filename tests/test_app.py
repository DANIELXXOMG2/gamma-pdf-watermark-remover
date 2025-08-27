import pytest
from httpx import AsyncClient
from app import app

@pytest.mark.asyncio
asnyc def test_read_main():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "<h1>Eliminador de Marcas de Agua de Gamma.ai</h1>" in response.text