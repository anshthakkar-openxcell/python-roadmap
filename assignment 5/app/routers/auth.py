from fastapi import APIRouter, Depends, HTTPException , BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.core.email import send_welcome_email
from app.schemas.user import UserCreate, UserLogin, Token
from app.crud.user import create_user, get_user_by_email
from app.core.security import verify_password, create_access_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
async def resgister_user(user: UserCreate, background_tasks: BackgroundTasks, db: AsyncSession = Depends(get_db)):
    existing_user = await get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = await create_user(db, user.email, user.password)
    background_tasks.add_task(send_welcome_email, user.email)
    return {"msg": "User created successfully", "user_id": new_user.id}

@router.post("/login", response_model=Token)
async def login_user(user: UserLogin, db: AsyncSession = Depends(get_db)):
    db_user = await get_user_by_email(db, user.email)

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token}


@router.get("/profile")
async def get_profile(current_user: str = Depends(get_current_user)):
    return {"email": current_user}


