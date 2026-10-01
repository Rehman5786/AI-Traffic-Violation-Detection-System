from sqlalchemy.orm import Session

from app.exceptions.custom_exceptions import (
    VehicleNotFoundException,
    VehicleRegistrationAlreadyExistsException,
)
from app.models.vehicle import Vehicle
from app.repositories.vehicle_repository import VehicleRepository


class VehicleService:
    """
    Business logic for vehicle management.

    Architecture:
        Route → Service → Repository → Database
    """

    def __init__(self, db: Session):
        self.repository = VehicleRepository(db)

    def get_by_id(self, vehicle_id: int) -> Vehicle | None:
        return self.repository.get_by_id(vehicle_id)

    def get_required_by_id(self, vehicle_id: int) -> Vehicle:
        vehicle = self.repository.get_by_id(vehicle_id)

        if vehicle is None:
            raise VehicleNotFoundException()

        return vehicle

    def get_by_registration_number(
        self,
        registration_number: str,
    ) -> Vehicle | None:
        normalized_registration = (
            registration_number.strip().upper()
        )

        return self.repository.get_by_registration_number(
            normalized_registration
        )

    def create_vehicle(
        self,
        registration_number: str,
        owner_name: str | None = None,
        vehicle_type: str | None = None,
        manufacturer: str | None = None,
        model: str | None = None,
        registration_date=None,
        status: str = "ACTIVE",
    ) -> Vehicle:
        normalized_registration = (
            registration_number.strip().upper()
        )

        existing_vehicle = (
            self.repository.get_by_registration_number(
                normalized_registration
            )
        )

        if existing_vehicle is not None:
            raise VehicleRegistrationAlreadyExistsException()

        vehicle = Vehicle(
            registration_number=normalized_registration,
            owner_name=owner_name.strip() if owner_name else None,
            vehicle_type=(
                vehicle_type.strip()
                if vehicle_type
                else None
            ),
            manufacturer=(
                manufacturer.strip()
                if manufacturer
                else None
            ),
            model=model.strip() if model else None,
            registration_date=registration_date,
            status=status.strip().upper(),
        )

        return self.repository.create(vehicle)

    def update_vehicle(
        self,
        vehicle: Vehicle,
        registration_number: str | None = None,
        owner_name: str | None = None,
        vehicle_type: str | None = None,
        manufacturer: str | None = None,
        model: str | None = None,
        registration_date=None,
        status: str | None = None,
    ) -> Vehicle:
        if registration_number is not None:
            normalized_registration = (
                registration_number.strip().upper()
            )

            if (
                normalized_registration
                != vehicle.registration_number
            ):
                existing_vehicle = (
                    self.repository.get_by_registration_number(
                        normalized_registration
                    )
                )

                if existing_vehicle is not None:
                    raise (
                        VehicleRegistrationAlreadyExistsException()
                    )

                vehicle.registration_number = (
                    normalized_registration
                )

        if owner_name is not None:
            vehicle.owner_name = owner_name.strip()

        if vehicle_type is not None:
            vehicle.vehicle_type = vehicle_type.strip()

        if manufacturer is not None:
            vehicle.manufacturer = manufacturer.strip()

        if model is not None:
            vehicle.model = model.strip()

        if registration_date is not None:
            vehicle.registration_date = registration_date

        if status is not None:
            vehicle.status = status.strip().upper()

        return self.repository.update(vehicle)

    def delete_vehicle(self, vehicle: Vehicle) -> None:
        self.repository.delete(vehicle)