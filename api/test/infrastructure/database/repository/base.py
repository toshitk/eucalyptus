from pytest import fixture
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.infrastructure.database.model.base import Base

# from src.infrastructure.database.model.user import Base as user


class RepositoryTestBase:
    @fixture
    async def _fixture(self):
        async_engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=True)
        async_session = sessionmaker(
            autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
        )
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

        # async def create_session():
        #     async with async_session() as session:
        #         yield session

        return async_session()
