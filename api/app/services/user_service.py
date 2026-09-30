from sqlalchemy.orm import Session


from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.exceptions.custom_exceptions import (
    EmailAlreadyExistsException,
    UserNotFoundException,
    UsernameAlreadyExistsException,
)


class UserService:
    """
    Business logic for user management.

    Architecture:
        Route → Service → Repository → Database
    """

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def get_by_id(self, user_id: int) -> User | None:
        return self.repository.get_by_id(user_id)

    def get_by_username(self, username: str) -> User | None:
        normalized_username = username.strip()

        return self.repository.get_by_username(
            normalized_username
        )

    def get_by_email(self, email: str) -> User | None:
        normalized_email = email.strip().lower()

        return self.repository.get_by_email(
            normalized_email
        )

    def create_user(
        self,
        username: str,
        email: str,
        password: str,
        full_name: str | None = None,
        role: str = "officer",
    ) -> User:
        normalized_username = username.strip()
        normalized_email = email.strip().lower()

        # Business rule: username must be unique.
        existing_username = self.repository.get_by_username(
            normalized_username
        )

        if existing_username is not None:
            raise ValueError(
                "Username already exists."
            )

        # Business rule: email must be unique.
        existing_email = self.repository.get_by_email(
            normalized_email
        )

        if existing_email is not None:
            raise ValueError(
                "Email already exists."
            )

        # Password hashing belongs to the service layer.
        hashed_password = hash_password(password)

        user = User(
            username=normalized_username,
            email=normalized_email,
            hashed_password=hashed_password,
            full_name=full_name.strip() if full_name else None,
            role=role.strip().lower(),
            is_active=True,
        )

        return self.repository.create(user)

    def update_user(
        self,
        user: User,
        username: str | None = None,
        email: str | None = None,
        full_name: str | None = None,
        role: str | None = None,
    ) -> User:
        if username is not None:
            normalized_username = username.strip()

            if normalized_username != user.username:
                existing_username = (
                    self.repository.get_by_username(
                        normalized_username
                    )
                )

                if existing_username is not None:
                    raise UsernameAlreadyExistsException()

                user.username = normalized_username

        if email is not None:
            normalized_email = email.strip().lower()

            if normalized_email != user.email:
                existing_email = self.repository.get_by_email(
                    normalized_email
                )

                if existing_email is not None:
                    raise EmailAlreadyExistsException()

                user.email = normalized_email

        if full_name is not None:
            user.full_name = full_name.strip()

        if role is not None:
            user.role = role.strip().lower()

        return self.repository.update(user)

    def change_password(
        self,
        user: User,
        new_password: str,
    ) -> User:
        user.hashed_password = hash_password(
            new_password
        )

        return self.repository.update(user)

    def activate_user(self, user: User) -> User:
        user.is_active = True

        return self.repository.update(user)

    def deactivate_user(self, user: User) -> User:
        user.is_active = False

        return self.repository.update(user)

    def delete_user(self, user: User) -> None:
        self.repository.delete(user)

    def get_required_by_id(self, user_id: int) -> User:
        user = self.repository.get_by_id(user_id)

        if user is None:
            raise UserNotFoundException()

        return user