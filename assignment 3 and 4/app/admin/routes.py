from fastapi import APIRouter, Depends
from app.core.security import verify_token

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)

@router.get("/dashboard", dependencies=[Depends(verify_token)])
async def secret_dashboard():
    return {
        "message": "Welcome Admin"
    }