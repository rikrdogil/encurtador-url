import json
import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from src.main import app 
pytestmark = pytest.mark.asyncio


async def test_para_validacao_tipo_parametro_errado():
    @app.get("/errado/{param}")
    def route_for_test(param: int) -> None:  # pragma: no cover
        pass

    async with AsyncClient(base_url="http://testserver", app=app) as client:
        response = await client.get("/errado/berg")

    assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY

    response_not_valid_int = {
    "detail": [
        {
            "loc": ["path", "param"],
            "msg": "value is not a valid integer",
            "type": "type_error.integer",
        }
    ]
}

    assert response_not_valid_int == response.json()
   
