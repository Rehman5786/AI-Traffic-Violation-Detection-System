from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.violation import Violation


class ViolationRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, violation_id: int) -> Violation | None:
        statement = select(Violation).where(
            Violation.id == violation_id
        )
        return self.db.scalar(statement)

    def get_by_license_plate(
        self,
        license_plate: str,
    ) -> list[Violation]:
        statement = select(Violation).where(
            Violation.license_plate == license_plate
        )
        return list(self.db.scalars(statement).all())

    def get_by_status(
        self,
        status: str,
    ) -> list[Violation]:
        statement = select(Violation).where(
            Violation.status == status
        )
        return list(self.db.scalars(statement).all())

    def create(self, violation: Violation) -> Violation:
        self.db.add(violation)
        self.db.commit()
        self.db.refresh(violation)
        return violation

    def update(self, violation: Violation) -> Violation:
        self.db.commit()
        self.db.refresh(violation)
        return violation

    def delete(self, violation: Violation) -> None:
        self.db.delete(violation)
        self.db.commit()