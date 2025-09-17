from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from pydantic import BaseModel

from sqllite import run_sql

@asynccontextmanager
async def lifespan(app: FastAPI):
    run_sql(
        """
        CREATE TABLE IF NOT EXISTS users (
            id_users            SERIAL PRIMARY KEY,
            password_users      VARCHAR(255) NOT NULL,
            name_users          VARCHAR(255) NOT NULL,
            email_users         VARCHAR(255) NOT NULL
        )
        """
    )
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

class User(BaseModel):
    password_users: str
    name_users: str
    email_users: str

@router.get("/")
def get_users():
    return run_sql("SELECT * FROM users")

@router.post("/users")
def create_users(body: User):
    password_users, name_users, email_users = body.password_users, body.name_users, body.email_users

    return run_sql(
        f"""
            INSERT INTO users(password_users, name_users, email_users) 
            VALUES('{password_users}', '{name_users}', '{email_users}')
        """
    )

@router.get("/users/{id_users}")
def get_user_by_id(id_users: int):
    result = run_sql(f"SELECT * FROM users WHERE id_users = {id_users}")
    if result:
        return result[0]  # Retorna o usuário
    return {"error": "Usuário não encontrado"}  # Caso não exista um usuário

@router.put("/users/{id_users}")
def update_user(id_users: int, body: User):
    password_users, name_users, email_users = body.password_users, body.name_users, body.email_users
    run_sql(
        f"""
        UPDATE users
        SET password_users = '{password_users}', name_users = '{name_users}', email_users = '{email_users}'
        WHERE id_users = {id_users}
        """
    )
    return {"message": "Usuário atualizado"}

@router.delete("/users/{id_users}")
def delete_user(id_users: int):
    run_sql(f"DELETE FROM users WHERE id_users = {id_users}")
    return {"message": "Usuário deletado"}

app.include_router(router=router)
