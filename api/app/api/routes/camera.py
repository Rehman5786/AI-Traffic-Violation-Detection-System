from fastapi import APIRouter


router = APIRouter(
    prefix="/cameras",
    tags=["Cameras"],
)


@router.get("/health")
def camera_health():
    return {
        "message": "Camera module is available",
    }