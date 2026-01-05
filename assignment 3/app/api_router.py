from fastapi import APIRouter
from app.inventory.routes import router as product_router
from app.admin.routes import router as admin_router

api_router = APIRouter()

api_router.include_router(product_router)
api_router.include_router(admin_router)