from app.schemas.product import ProductCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import Product

async def create_product(product_in : ProductCreate, db : AsyncSession)->Product:
    product = Product(**product_in.model_dump())
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product