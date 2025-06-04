
# API Embrapa - Tech Challenge Fase 1

Projeto desenvolvido para o Tech Challenge da pós-graduação em Machine Learning Engineering (PosTech - FIAP).

## 🚀 Problema

Você foi contratado por uma consultoria para extrair e disponibilizar, via API pública, os dados de vitivinicultura do site da Embrapa. Esses dados envolvem produção, processamento, comercialização, importação e exportação, e servirão futuramente como base para um modelo de Machine Learning.

---

## 📦 Stack utilizada

- Python 3.11
- FastAPI
- Uvicorn
- BeautifulSoup4
- Pandas
- JWT (Autenticação)
- Render (Deploy)

---

## 📁 Estrutura do projeto

```
projeto_embrapa/
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── tabelas.py
│   ├── services/
│   │   └── leitor_csv.py
│   ├── auth/
│   │   └── jwt.py
├── tabelas_embrapa/
│   └── *.csv  ← dados extraídos via scraper
├── requirements.txt
```

---

## 🔐 Autenticação

- Rota `/login` com usuário: `admin` e senha: `1234`
- Use o token JWT retornado para acessar os endpoints protegidos (Desativado)

---

## 🛠️ Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repo.git
cd projeto_embrapa

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Rode a API
uvicorn app.main:app --reload
```

Acesse em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 Como rodar testes (opcional)

Caso deseje incluir testes, crie a pasta `tests/` com arquivos `test_*.py` e execute:

```bash
pytest
```

---

## 🌐 Link do Deploy

🔗 [Link para a API](https://api-embrapa-tech-challenge-mrhx.onrender.com/docs)

---

## 📺 Vídeo de apresentação

🎥 [Link para o vídeo de apresentação no YouTube](https://youtu.be/dxJsp6q9qhM)

---

## 📊 Diagrama de Arquitetura

📎 ![[Link para o diagrama - draw.io, PNG ou PDF](https://seulink.com/diagrama)](https://github.com/Luc45-S1lva/api-embrapa-tech-challenge/blob/1371979e1eeba23794491a0908af77140f156f3c/Fluxograma_Embrapa.drawio.png)

---

## 💡 Extras implementados

- Estrutura modularizada
- Filtros por coluna nos CSVs (`/tabelas/filtro`)
- Autenticação JWT
- Fallback com arquivos locais caso o site da Embrapa esteja fora do ar
- Pronto para integrar com dashboard ou ML pipeline

---

## 📢 Equipe

**Lucas Silva** RM361127 5MLET

---
