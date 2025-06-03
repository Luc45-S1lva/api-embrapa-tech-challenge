import os
import pandas as pd

CAMINHO = "tabelas_embrapa"

def listar_arquivos_csv():
    return [f for f in os.listdir(CAMINHO) if f.endswith(".csv")]

def ler_csv(nome_arquivo):
    caminho = os.path.join(CAMINHO, nome_arquivo)
    if not os.path.exists(caminho):
        raise FileNotFoundError("Arquivo não encontrado")
    df = pd.read_csv(caminho)
    return df.to_dict(orient="records")

def ler_csv_filtrado(nome_arquivo, coluna, valor):
    caminho = os.path.join(CAMINHO, nome_arquivo)
    if not os.path.exists(caminho):
        raise FileNotFoundError("Arquivo não encontrado")
    df = pd.read_csv(caminho)
    if coluna not in df.columns:
        raise ValueError("Coluna não encontrada")
    filtrado = df[df[coluna].astype(str).str.contains(valor, case=False, na=False)]
    return filtrado.to_dict(orient="records")
