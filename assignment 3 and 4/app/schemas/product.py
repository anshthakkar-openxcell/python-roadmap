from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    name: str
    price: float = Field(..., gt=0)
    category: str
    description: str | None = None


class ProductCreate(ProductBase):
    pass



class ProductRead(ProductBase):
    id: int

    class Config:
        from_attributes = True