import json
from fastapi import APIRouter, Depends
from app.core.redis import redis_client
from app.crud.trending import get_trending_from_db
from app.core.security import get_current_user

router = APIRouter(prefix="/trending", tags=["Trending"])

CACHE_KEY = "trending_data"
CACHE_TTL = 60  # seconds

@router.get("/")
async def trending():
    # check Redis
    cached = await redis_client.get(CACHE_KEY)

    if cached:
        return {
            "source": "cache",
            "data": json.loads(cached)
        }

   
    data = await get_trending_from_db()

    # store in Redis
    await redis_client.set(
        CACHE_KEY,
        json.dumps(data),
        ex=CACHE_TTL
    )

    return {
        "source": "database",
        "data": data
    }
