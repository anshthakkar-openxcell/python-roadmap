from sqlmodel import SQLModel, Field
from typing import Optional


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    name: str
    bio: Optional[str] = None
    


# from sqlalchemy import String,Float
# from sqlalchemy.orm import Mapped,mapped_column
# from app.db.base import Base

# class User(Base):
#     __tablename__ = "users"

#     id : Mapped[int] =mapped_column(primary_key=True)
#     email : Mapped[str] = mapped_column(String(255),nullable=False,unique=True,index=True)
#     name : Mapped[str] = mapped_column(String(100),nullable=False)
#     bio : Mapped[str|None] = mapped_column(nullable=True)