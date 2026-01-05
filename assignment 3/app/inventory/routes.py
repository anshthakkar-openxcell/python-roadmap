from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.product import ProductCreate
from app.inventory.service import create_product

router = APIRouter(prefix="/products",tags=["products"])


@router.post("/")
async def add_product(
    product:ProductCreate,
    db:AsyncSession= Depends(get_db)
):
    return await create_product(product,db)