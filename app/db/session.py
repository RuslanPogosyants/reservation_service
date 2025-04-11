from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine

engine: AsyncEngine = create_async_engine('postgresql+asyncpg://postgres:postgre@localhost:5432/reservation_db')


AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
