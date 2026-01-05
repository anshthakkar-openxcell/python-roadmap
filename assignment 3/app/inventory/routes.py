from fastapi import APIRouter, Depends,HTTPException ,Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import verify_token

from app.db.session import get_db
from app.schemas.product import ProductCreate
from app.inventory.service import create_product,get_producty_by_id,fetch_products

router = APIRouter(prefix="/products",tags=["products"])



@router.post("/")
async def add_product(
    product:ProductCreate,
    db:AsyncSession= Depends(get_db)
):
    return await create_product(product,db)


@router.get("/")
async def list_products(
    category: str | None =Query(default = None),
    limit:int = Query(default=10,le=100),
    db : AsyncSession = Depends(get_db)
):
    return await fetch_products(db, category, limit)


@router.get("/{product_id}")
async def get_product(
    product_id :int,
    db :AsyncSession = Depends(get_db)
):
    product = await get_producty_by_id(db,product_id)
    if not product:
        raise HTTPException(status_code=404,detail="Product not found")
    return product



