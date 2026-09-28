from fastapi import APIRouter


router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"],
)


@router.get("/health")
def notification_health():
    return {
        "message": "Notification module is available",
    }