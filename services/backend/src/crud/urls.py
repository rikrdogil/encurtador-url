
import os
from tabnanny import check
from typing import Any
from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.config.models import Urls
from src.schemas.urls import UrlOutSchema,UrlRedirectSchema,UrlRedirectSchema, CreateUrl,UrlInSchema
from src.schemas.token import Status
import shortuuid 
from datetime import date, datetime, time, timedelta
from fastapi_pagination.ext.tortoise import paginate

async def get_urls() -> UrlOutSchema:
    return await paginate(Urls.all().order_by("-id"))


async def redirect_url(codigo_url) -> UrlRedirectSchema:
    return await UrlRedirectSchema.from_queryset_single(Urls.get(codigoUrl=codigo_url))


async def create_url(url) -> UrlOutSchema:
    url_dict = url.dict(exclude_unset=True)
    if not url_dict["url"]:
       raise HTTPException(status_code = 400, detail = "Url é obrigatório.")
    
    if url_dict["codigoUrl"]:
        codigoUrl = url_dict["codigoUrl"]
    
    else:
        codigoUrl = shortuuid.ShortUUID().random(length = 4)    
    
    if not url_dict["dataExpiracao"]:
        data_expiracao = datetime.now().date() + timedelta(days=7)
    
    else:
        data_expiracao = url_dict["dataExpiracao"]
    
    urlEncurtada = os.path.join(os.environ.get("BASE_URL"), codigoUrl)
    check_codigo =  await Urls.filter(codigoUrl=codigoUrl).first()
    
    if check_codigo is not None:
        raise HTTPException(status_code = 400, detail = "O código informado já está em uso,tente outro")
    
    try:
        url_dict["codigoUrl"] = codigoUrl
        url_dict["urlEncurtada"] = urlEncurtada
        url_dict["dataExpiracao"] =  data_expiracao
        url_obj = await Urls.create(**url_dict)
        return await UrlOutSchema.from_tortoise_orm(url_obj)

    except Exception as e:
        raise HTTPException(status_code = 500, detail = "Aconteceu um erro desconhecido.")
  
    return await UrlOutSchema.from_tortoise_orm(url_obj)