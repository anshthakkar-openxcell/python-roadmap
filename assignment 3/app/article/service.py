from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.models.article import Article


async def create_article_service(db: AsyncSession, article:Article) -> Article:
    db.add(article)

    try:
        await db.commit()
        await db.refresh(article)
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=500, detail="Error creating article")

    return article

async def get_articles_for_user(db: AsyncSession, user_id: int) -> list[Article]:
    result = await db.execute(select(Article).where(Article.user_id == user_id))
    articles = result.scalars().all()
    return articles