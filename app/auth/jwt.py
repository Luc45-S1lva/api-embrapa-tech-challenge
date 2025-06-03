from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

router = APIRouter(tags=["Autenticação"])

SECRET_KEY = "supersecreto"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

fake_user = {
    "username": "admin",
    "hashed_password": "$2b$12$XcgG1o3M28GHqGoHH0CPluM36IX8M6soMjK5q7whYOi6rOwzHZdXS"  # senha: 1234
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def verificar_senha(plain, hashed):
    return pwd_context.verify(plain, hashed)

def criar_token(data: dict, exp=None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (exp or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != fake_user["username"] or not verificar_senha(form_data.password, fake_user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Usuário ou senha inválidos")
    token = criar_token({"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("sub") != fake_user["username"]:
            raise HTTPException(status_code=401, detail="Usuário inválido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
