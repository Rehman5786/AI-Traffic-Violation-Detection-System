from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.camera import Camera


class CameraRepository:
    """
    Database access layer for Camera entities.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, camera_id: int) -> Camera | None:
        """
        Retrieve a camera by primary key.
        """
        statement = select(Camera).where(
            Camera.id == camera_id
        )

        return self.db.scalar(statement)

    def get_active_cameras(self) -> list[Camera]:
        """
        Retrieve all active cameras.
        """
        statement = select(Camera).where(
            Camera.is_active.is_(True)
        )

        return list(self.db.scalars(statement).all())

    def create(self, camera: Camera) -> Camera:
        """
        Persist a new camera.
        """
        self.db.add(camera)
        self.db.commit()
        self.db.refresh(camera)

        return camera

    def update(self, camera: Camera) -> Camera:
        """
        Persist changes to an existing camera.
        """
        self.db.commit()
        self.db.refresh(camera)

        return camera

    def delete(self, camera: Camera) -> None:
        """
        Delete a camera.
        """
        self.db.delete(camera)
        self.db.commit()