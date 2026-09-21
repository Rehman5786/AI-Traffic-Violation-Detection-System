from sqlalchemy import text

from app.db.session import engine


def init_db() -> None:
    """
    Initialize the database connection and verify availability.

    Table creation will be handled later through Alembic migrations.
    """
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    print("Database connection verified successfully.")