import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette.status import HTTP_404_NOT_FOUND

from src.main import app 
pytestmark = pytest.mark.asyncio


async def test_endpoit_errado():
    async with AsyncClient(base_url="http://testserver", app=app) as client:
        response = await client.get("/errado/asd")

    assert response.status_code == HTTP_404_NOT_FOUND

    error_data = response.json()
    assert response.json() == {"detail": "Not Found"}
