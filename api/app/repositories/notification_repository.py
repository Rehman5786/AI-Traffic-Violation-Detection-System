from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.notification import Notification


class NotificationRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(
        self,
        notification_id: int,
    ) -> Notification | None:
        statement = select(Notification).where(
            Notification.id == notification_id
        )
        return self.db.scalar(statement)

    def get_by_violation_id(
        self,
        violation_id: int,
    ) -> list[Notification]:
        statement = select(Notification).where(
            Notification.violation_id == violation_id
        )
        return list(self.db.scalars(statement).all())

    def get_by_status(
        self,
        status: str,
    ) -> list[Notification]:
        statement = select(Notification).where(
            Notification.status == status
        )
        return list(self.db.scalars(statement).all())

    def create(
        self,
        notification: Notification,
    ) -> Notification:
        self.db.add(notification)
        self.db.commit()
        self.db.refresh(notification)
        return notification

    def update(
        self,
        notification: Notification,
    ) -> Notification:
        self.db.commit()
        self.db.refresh(notification)
        return notification

    def delete(
        self,
        notification: Notification,
    ) -> None:
        self.db.delete(notification)
        self.db.commit()