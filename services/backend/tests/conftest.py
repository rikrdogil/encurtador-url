from os import environ

import pytest
from asgi_lifespan import LifespanManager
from asyncpg.pool import Pool
from fastapi import FastAPI
from httpx import AsyncClient
from jose import JWTError, jwt

from src.crud.urls import create_url, get_urls, redirect_url
from src.crud.users import create_user
from src.config.models import Urls
from src.config.models import Users
from src.schemas.users import UserOut
from src.schemas.urls import CreateUrl
from src.auth import jwthandler
from tests.fake_asyncpg_pool import FakeAsyncPGPool
from src.main import app 
environ["APP_ENV"] = "test"


#@pytest.fixture
#def app() -> FastAPI:
  # importação local para fins de teste




@pytest.fixture
async def initialized_app(app: app) -> FastAPI:
    async with LifespanManager(app):
        app.state.pool = await FakeAsyncPGPool.create_pool(app.state.pool)
        yield app


@pytest.fixture
def pool(initialized_app: FastAPI) -> Pool:
    return initialized_app.state.pool


@pytest.fixture
async def client(initialized_app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        app=initialized_app,
        base_url="http://testserver",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client



@pytest.fixture
async def test_user(pool: Pool) -> UserOut:
        return await create_user(
            full_name="full_name", password="password", username="username"
        )


@pytest.fixture
async def test_url(pool: Pool) -> CreateUrl:
        return await create_url(
            url ="https://docs.pytest.org/en/6.2.x/contents.html",
            codigoUrl="",
            dataExpiracao="",
        )


@pytest.fixture
def token(test_user: UserOut) -> str:
    return jwthandler.create_access_token(test_user)


@pytest.fixture
def authorized_client(
    client: AsyncClient, token: str
) -> AsyncClient:
    client.headers = {
        "Authorization": f"Bearer {token}",
        **client.headers,
    }
    return client
