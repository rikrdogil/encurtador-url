import queue
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config.models import Urls
from src.schemas.urls import UrlInSchema
from tortoise import Tortoise
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi_pagination import add_pagination

from src.config.register import register_tortoise
from src.config.database import TORTOISE_ORM
from src.routes import users, urls

from datetime import date, datetime, time, timedelta

Tortoise.init_models(["src.config.models"], "models")

app = FastAPI()

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users.router)
app.include_router(urls.router)

add_pagination(app)

# configuracao tamanho da fila   
app.queue_system = queue.Queue()
app.queue_limit = 2

# metodo que remove urls com data de expiracao anteriores ao dia atual 
async def removeUrls():
    for i in range(app.queue_limit):
        if  app.queue_system.empty():
            data_atual = datetime.now().date()
            urls = await Urls.filter(dataExpiracao__lt=data_atual).delete()
            if not urls:            
                print('as urls expiradas foram removidas')

# agendador de tarefa configurado para remover urls expiradas diariamente            
app.scheduler = AsyncIOScheduler()
app.scheduler.add_job(removeUrls, 'interval', days=1)
app.scheduler.start()

@app.get("/")
def home():
    return "Encurtador de Url"
