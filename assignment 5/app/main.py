from fastapi import FastAPI
from app.routers import auth, trending
from app.db.session import engine
from app.db.base import Base
app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
app.include_router(auth.router)
app.include_router(trending.router)