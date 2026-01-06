import asyncio

async def get_trending_from_db():
    # simulate heavy DB query
    await asyncio.sleep(3)

    return [
        {"id": 1, "title": "FastAPI Security"},
        {"id": 2, "title": "Redis Caching"},
        {"id": 3, "title": "Async SQLAlchemy"},
    ]