# Encurtador de URL FastUrl

O projeto de uma API encurtadora de Url em FastAPI e
Vue.js como frontEnd

## Implementação

As URLs encurtadas possuem um tempo de expiração padrão (7 dias) e após esse periodo elas 
são removidas da base de dados

BackEnd:
A API possui 2 endpoints:
1. Criação de URL encurtada
Parâmetros:
- URL original
- URL encurtada desejada (opcional, padrão é randômico)
- Data de expiração (opcional, padrão é expirar em 7 dias)
Retorno (JSON):
- URL encurtada

2. URL encurtada
Não recebe parâmetros, apenas redireciona para a URL original

Frontend:

Aplicação Frontend  Vue.js que permite a criação de url encurta, cadastro e autenticação através de usuário
e senha para exibição de todas as URLs encurtadas.




## Instalação

```
$ docker-compose up -d --build
```

```
$ docker-compose exec backend aerich upgrade
```



## Informações complementares 

Container BackEnd:
Framework: [FastAPI](https://fastapi.tiangolo.com/)
ORM: [Tortoise ORM](https://tortoise-orm.readthedocs.io/en/latest/)
Web server: [Uvicorn](https://www.uvicorn.org/)
Gerenciador de dependencias: [Poetry](https://python-poetry.org/)
Testes: [Pytest](https://docs.pytest.org/en/7.0.x/contents.html)

Container Frontend:
JavaScript Framework: [Vue.js](https://vuejs.org/)
Vue UI: [Vuetify](https://vuetifyjs.com/en/)
Web server: [Nginx](https://nginx.org/en/docs/)

Container DataBase:
[Postgres](https://www.postgresql.org/)


## Acessando API

[http://localhost:8000/docs](http://localhost:8000/docs).

## Acessando Aplicação

[http://localhost/](http://localhost/).



