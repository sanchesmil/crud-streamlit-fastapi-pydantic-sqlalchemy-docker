from fastapi import FastAPI
from database import engine
import models
from router import router

# cria a tabela efetivamente
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# importa o arquivo de rotas
app.include_router(router)