from sqlalchemy.orm import Session

from app.exceptions.custom_exceptions import (
    CameraNameAlreadyExistsException,
    CameraNotFoundException,
)
from app.models.camera import Camera
from app.repositories.camera_repository import CameraRepository


class CameraService:
    """
    Business logic for camera management.

    Architecture:
        Route → Service → Repository → Database
    """

    def __init__(self, db: Session):
        self.repository = CameraRepository(db)

    def get_by_id(self, camera_id: int) -> Camera | None:
        return self.repository.get_by_id(camera_id)

    def get_required_by_id(self, camera_id: int) -> Camera:
        camera = self.repository.get_by_id(camera_id)

        if camera is None:
            raise CameraNotFoundException()

        return camera

    def get_by_name(self, name: str) -> Camera | None:
        normalized_name = name.strip()

        return self.repository.get_by_name(
            normalized_name
        )

    def get_active_cameras(self) -> list[Camera]:
        return self.repository.get_active_cameras()

    def create_camera(
        self,
        name: str,
        location: str,
        latitude: float | None = None,
        longitude: float | None = None,
        stream_url: str | None = None,
        device_type: str = "Raspberry Pi Camera",
        is_active: bool = True,
    ) -> Camera:
        normalized_name = name.strip()

        existing_camera = self.repository.get_by_name(
            normalized_name
        )

        if existing_camera is not None:
            raise CameraNameAlreadyExistsException()

        camera = Camera(
            name=normalized_name,
            location=location.strip(),
            latitude=latitude,
            longitude=longitude,
            stream_url=stream_url.strip()
            if stream_url
            else None,
            device_type=device_type.strip(),
            is_active=is_active,
        )

        return self.repository.create(camera)

    def update_camera(
        self,
        camera: Camera,
        name: str | None = None,
        location: str | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        stream_url: str | None = None,
        device_type: str | None = None,
        is_active: bool | None = None,
    ) -> Camera:
        if name is not None:
            normalized_name = name.strip()

            if normalized_name != camera.name:
                existing_camera = self.repository.get_by_name(
                    normalized_name
                )

                if existing_camera is not None:
                    raise CameraNameAlreadyExistsException()

                camera.name = normalized_name

        if location is not None:
            camera.location = location.strip()

        if latitude is not None:
            camera.latitude = latitude

        if longitude is not None:
            camera.longitude = longitude

        if stream_url is not None:
            camera.stream_url = stream_url.strip()

        if device_type is not None:
            camera.device_type = device_type.strip()

        if is_active is not None:
            camera.is_active = is_active

        return self.repository.update(camera)

    def activate_camera(self, camera: Camera) -> Camera:
        camera.is_active = True

        return self.repository.update(camera)

    def deactivate_camera(self, camera: Camera) -> Camera:
        camera.is_active = False

        return self.repository.update(camera)

    def delete_camera(self, camera: Camera) -> None:
        self.repository.delete(camera)