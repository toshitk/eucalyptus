from contextlib import asynccontextmanager
from typing import Callable

from pytest import fixture
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Session, sessionmaker
from src.infrastructure.database.model.base import Base



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

        return async_session()

    @asynccontextmanager
    async def setup_method(
        self, session: Session, func: Callable | None = None, rollback: bool = True
    ):
        try:
            if func is not None:
                yield await func()
            else:
                yield None
        finally:
            if rollback:
                await session.rollback()
                await session.close()
            else:
                await session.commit()
                await session.close()
