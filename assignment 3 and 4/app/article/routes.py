from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.article.service import create_article_service, get_articles_for_user
from app.models.article import Article
from app.schemas.article import ArticleRead

router = APIRouter(prefix="/articles", tags=["Articles"])


@router.post("/", response_model=Article)
async def create_article(article: Article, db: AsyncSession = Depends(get_db)):
    return await create_article_service(db, article)

@router.get("/user/{user_id}", response_model=list[ArticleRead])
async def list_user_articles(
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    return await get_articles_for_user(db, user_id)
