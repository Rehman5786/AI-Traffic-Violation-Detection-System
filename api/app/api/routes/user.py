from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/health")
def user_health():
    return {
        "message": "User module is available",
    }