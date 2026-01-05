from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from fastapi import HTTPException

from app.models.user import User

async def create_user_service(db: AsyncSession, user:User)-> User:
    existing_user = await db.execute(select(User).where(User.email == user.email))
    existing_user = existing_user.scalars().first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    db.add(user)

    try:
        await db.commit()
        await db.refresh(user)
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=500,detail="Error creating user")
    
    return user


async def get_user_service(db :AsyncSession,user_id:int) ->User:
    result =  await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()



    if not user:
        raise HTTPException(status_code=404,description="User not found")
    

    return user