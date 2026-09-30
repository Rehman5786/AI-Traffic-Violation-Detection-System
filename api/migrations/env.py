from logging.config import fileConfig

from alembic import context

from app.db.base import Base
from app.db.session import engine

from app.db.base import Base
from app.db.session import engine

# Import all ORM models so Alembic can discover them.
from app.models.user import User  # noqa: F401, E402
from app.models.vehicle import Vehicle  # noqa: F401, E402
from app.models.camera import Camera  # noqa: F401, E402
from app.models.violation import Violation  # noqa: F401, E402
from app.models.evidence import Evidence  # noqa: F401, E402
from app.models.notification import Notification  # noqa: F401, E402
from app.models.audit_log import AuditLog  # noqa: F401, E402


# Alembic Config object
config = context.config


# Configure Python logging from alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# SQLAlchemy metadata used by Alembic autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """
    Run migrations in offline mode.

    Alembic generates SQL without establishing a database connection.
    """
    url = engine.url.render_as_string(hide_password=False)

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """
    Run migrations in online mode.

    Uses the application's existing SQLAlchemy engine.
    """
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()