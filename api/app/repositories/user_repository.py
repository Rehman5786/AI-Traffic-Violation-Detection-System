from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    """
    Database access layer for User entities.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: int) -> User | None:
        """
        Retrieve a user by primary key.
        """
        statement = select(User).where(User.id == user_id)

        return self.db.scalar(statement)

    def get_by_username(self, username: str) -> User | None:
        """
        Retrieve a user by username.
        """
        statement = select(User).where(
            User.username == username
        )

        return self.db.scalar(statement)

    def get_by_email(self, email: str) -> User | None:
        """
        Retrieve a user by email.
        """
        statement = select(User).where(
            User.email == email
        )

        return self.db.scalar(statement)

    def create(self, user: User) -> User:
        """
        Persist a new user.
        """
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def update(self, user: User) -> User:
        """
        Persist changes to an existing user.
        """
        self.db.commit()
        self.db.refresh(user)

        return user

    def delete(self, user: User) -> None:
        """
        Delete a user.
        """
        self.db.delete(user)
        self.db.commit()