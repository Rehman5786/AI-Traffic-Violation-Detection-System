from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.vehicle import Vehicle


class VehicleRepository:
    """
    Database access layer for Vehicle entities.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, vehicle_id: int) -> Vehicle | None:
        """
        Retrieve a vehicle by primary key.
        """
        statement = select(Vehicle).where(
            Vehicle.id == vehicle_id
        )

        return self.db.scalar(statement)

    def get_by_registration_number(
        self,
        registration_number: str,
    ) -> Vehicle | None:
        """
        Retrieve a vehicle by registration number.
        """
        statement = select(Vehicle).where(
            Vehicle.registration_number == registration_number
        )

        return self.db.scalar(statement)

    def create(self, vehicle: Vehicle) -> Vehicle:
        """
        Persist a new vehicle.
        """
        self.db.add(vehicle)
        self.db.commit()
        self.db.refresh(vehicle)

        return vehicle

    def update(self, vehicle: Vehicle) -> Vehicle:
        """
        Persist changes to an existing vehicle.
        """
        self.db.commit()
        self.db.refresh(vehicle)

        return vehicle

    def delete(self, vehicle: Vehicle) -> None:
        """
        Delete a vehicle.
        """
        self.db.delete(vehicle)
        self.db.commit()