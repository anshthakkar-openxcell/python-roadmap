# app/schemas/article.py
from sqlmodel import SQLModel

class ArticleRead(SQLModel):
    id: int
    title: str
    content: str

class ArticleCreate(SQLModel):
    title: str
    content: str
    user_id: int