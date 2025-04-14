import asyncio
import os
from logging.config import fileConfig
from dotenv import load_dotenv

from alembic import context
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config
from app.db.models import Base

load_dotenv()

if context.config.config_file_name is not None:
    fileConfig(context.config.config_file_name)


target_metadata = Base.metadata


def get_database_url():
    return os.getenv("DATABASE_URL")


def run_migrations_offline():
    context.configure(
        url=get_database_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    configuration = {"sqlalchemy.url": get_database_url(), "sqlalchemy.echo": "True"}

    connectable = async_engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )
    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
