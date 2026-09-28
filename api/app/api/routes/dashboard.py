from fastapi import APIRouter


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/health")
def dashboard_health():
    return {
        "message": "Dashboard module is available",
    }