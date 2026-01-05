from fastapi import APIRouter ,Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.models.user import User
from app.user.service import (get_user_service,create_user_service)



router = APIRouter(prefix="/users",tags=["Users"])


@router.post("/",response_model=User)
async def create_user(
    user: User,
    db: AsyncSession = Depends(get_db)
):
    return await create_user_service(db ,user)


@router.get("/user_id}",response_model=User)
async def get_user(
    user_id :int,
    db: AsyncSession =Depends(get_db)
    
):
    return await get_user_service(db,user_id)