from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from app.models.user import User


class Article(SQLModel, table=True):
    id:Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str

    user_id: int = Field(foreign_key="user.id")
    user: "User" = Relationship(back_populates="articles")