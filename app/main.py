from fastapi import FastAPI
from app.routes import tabelas
from app.auth import jwt

app = FastAPI(title="API Embrapa - Fase 1")

app.include_router(jwt.router)
app.include_router(tabelas.router)

@app.get("/")
def root():
    return {"mensagem": "API da Embrapa com JWT e Filtros está no ar 🚀"}
