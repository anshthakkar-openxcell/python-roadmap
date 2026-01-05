from app.schemas.product import ProductCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import Product
from sqlalchemy import select

async def create_product(product_in : ProductCreate, db : AsyncSession)->Product:
    product = Product(**product_in.model_dump())
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product



async def get_producty_by_id(db:AsyncSession,product_id:int):
    result = await db.execute(select(Product).where(Product.id==product_id))
    return result.scalar_one_or_none()


async def fetch_products(
    db: AsyncSession,
    category: str | None = None,
    limit: int = 10,
):
    stmt = select(Product)

    if category:
        stmt = stmt.where(Product.category == category)

    stmt = stmt.limit(limit)

    result = await db.execute(stmt)
    return result.scalars().all()

