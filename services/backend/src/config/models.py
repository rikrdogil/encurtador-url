
from datetime import datetime, timedelta
from tortoise import fields, models


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    full_name = fields.CharField(max_length=50, null=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class Urls(models.Model):   
    id = fields.IntField(pk=True)
    url = fields.CharField(max_length=225, null=False)
    codigoUrl = fields.CharField(max_length=225, null=True)
    urlEncurtada = fields.CharField(max_length=225, null=True)
    dataExpiracao =  fields.DateField(null=True)
    #dataCriacao = fields.DateField(auto_now_add=True)
   
