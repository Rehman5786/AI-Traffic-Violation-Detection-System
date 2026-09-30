from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.evidence import Evidence


class EvidenceRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, evidence_id: int) -> Evidence | None:
        statement = select(Evidence).where(
            Evidence.id == evidence_id
        )
        return self.db.scalar(statement)

    def get_by_violation_id(
        self,
        violation_id: int,
    ) -> list[Evidence]:
        statement = select(Evidence).where(
            Evidence.violation_id == violation_id
        )
        return list(self.db.scalars(statement).all())

    def create(self, evidence: Evidence) -> Evidence:
        self.db.add(evidence)
        self.db.commit()
        self.db.refresh(evidence)
        return evidence

    def update(self, evidence: Evidence) -> Evidence:
        self.db.commit()
        self.db.refresh(evidence)
        return evidence

    def delete(self, evidence: Evidence) -> None:
        self.db.delete(evidence)
        self.db.commit()