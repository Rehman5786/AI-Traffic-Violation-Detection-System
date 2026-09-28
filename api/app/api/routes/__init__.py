from fastapi import APIRouter

from app.api.routes.auth import router as auth_router
from app.api.routes.user import router as user_router
from app.api.routes.vehicle import router as vehicle_router
from app.api.routes.camera import router as camera_router
from app.api.routes.violation import router as violation_router
from app.api.routes.notification import router as notification_router
from app.api.routes.dashboard import router as dashboard_router


api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(user_router)
api_router.include_router(vehicle_router)
api_router.include_router(camera_router)
api_router.include_router(violation_router)
api_router.include_router(notification_router)
api_router.include_router(dashboard_router)