from fastapi import APIRouter, Depends, HTTPException
from app.services import leitor_csv
from app.auth.jwt import get_current_user

router = APIRouter(prefix="/tabelas", tags=["Tabelas"])

@router.get("/")

def listar_tabelas():
    return leitor_csv.listar_arquivos_csv()

@router.get("/{nome_arquivo}", dependencies=[Depends(get_current_user)])
def ler_tabela(nome_arquivo: str):
    return leitor_csv.ler_csv(nome_arquivo)

@router.get("/filtro/{nome_arquivo}", dependencies=[Depends(get_current_user)])
def ler_com_filtro(nome_arquivo: str, coluna: str, valor: str):
    return leitor_csv.ler_csv_filtrado(nome_arquivo, coluna, valor)
