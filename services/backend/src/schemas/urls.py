import datetime
from typing import Optional,List
from fastapi import Body
from datetime import date, datetime, time, timedelta
from pydantic import BaseModel,validator, constr
from tortoise.contrib.pydantic import pydantic_model_creator

from src.config.models import Urls
import validators


UrlInSchema = pydantic_model_creator(
    Urls, name="UrlIn", exclude_readonly=True)


UrlOutSchema = pydantic_model_creator(
    Urls, name="Url", exclude =[
      "id","url","codigoUrl"
    ]
)


UrlRedirectSchema = pydantic_model_creator(
    Urls, name="UrlRedirect", exclude =[
      "id", "dataExpiracao","codigoUrl", "dataExpiracao","urlEncurtada"
    ]
)


class UrlIn(BaseModel):
    url: str
    codigoUrl: str
    dataExpiracao:Optional[date] = None
    urlEncurtada:Optional[str] = None


class UrlOut(UrlIn):
    class Config:
        orm_mode = True


class CreateUrl(BaseModel):
    url: str
    codigoUrl: Optional[str] = None
    dataExpiracao: Optional[str] = None

    @validator('url')
    def validate_url(cls, v):
        if not validators.url(v):  raise ValueError("Url informada é invalida.")
        return v