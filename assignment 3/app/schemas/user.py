# app/schemas/user.py
from typing import Optional, List
from sqlmodel import SQLModel
from app.schemas.article import ArticleRead

class UserCreate(SQLModel):
    email: str
    name: str
    bio: Optional[str] = None

class UserRead(SQLModel):
    id: int
    email: str
    name: str
    bio: Optional[str]
    articles: List[ArticleRead] = []
