from fastapi import APIRouter


router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"],
)


@router.get("/health")
def vehicle_health():
    return {
        "message": "Vehicle module is available",
    }