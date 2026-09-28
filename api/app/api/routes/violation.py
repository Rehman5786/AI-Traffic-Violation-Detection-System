from fastapi import APIRouter


router = APIRouter(
    prefix="/violations",
    tags=["Violations"],
)


@router.get("/health")
def violation_health():
    return {
        "message": "Violation module is available",
    }