from typing import List
from unicodedata import name
from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist
from fastapi_pagination import LimitOffsetPage, Page, add_pagination

import src.crud.urls as crud
from src.auth.jwthandler import get_current_user
from src.schemas.urls import UrlInSchema, UrlOutSchema, CreateUrl,UrlRedirectSchema, UrlOut
from src.schemas.token import Status
from src.schemas.users import UserOut

router = APIRouter(tags=["urls"])


@router.get(
    "/urls",
   response_model=Page[UrlOut],
   dependencies=[Depends(get_current_user)],
   name="urls:get-all"
)
async def get_urls():
    return await crud.get_urls()


@router.get(
     "/{codigo_url}",
     response_model=UrlRedirectSchema,
     name="url:get-codigo-for-redirect",
 )
async def get_url(codigo_url: str) -> UrlRedirectSchema:
    try:
        return await crud.redirect_url(codigo_url)
    except DoesNotExist:
        raise HTTPException(
             status_code=404,
             detail="Url encurtada não existe",
         )


@router.post(                                                                                   
    "/url", response_model=UrlOutSchema, name="urls:create-url",                     
)
async def create_url(
    url: CreateUrl,
) -> UrlOutSchema:
    return await crud.create_url(url)
