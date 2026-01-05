from fastapi import FastAPI
from app.api_router import api_router
from app.db.base import Base
from app.db.session import engine

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(api_router)