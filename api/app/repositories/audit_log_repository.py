from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog


class AuditLogRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(
        self,
        audit_log_id: int,
    ) -> AuditLog | None:
        statement = select(AuditLog).where(
            AuditLog.id == audit_log_id
        )
        return self.db.scalar(statement)

    def get_by_user_id(
        self,
        user_id: int,
    ) -> list[AuditLog]:
        statement = select(AuditLog).where(
            AuditLog.user_id == user_id
        )
        return list(self.db.scalars(statement).all())

    def get_by_action(
        self,
        action: str,
    ) -> list[AuditLog]:
        statement = select(AuditLog).where(
            AuditLog.action == action
        )
        return list(self.db.scalars(statement).all())

    def create(
        self,
        audit_log: AuditLog,
    ) -> AuditLog:
        self.db.add(audit_log)
        self.db.commit()
        self.db.refresh(audit_log)
        return audit_log