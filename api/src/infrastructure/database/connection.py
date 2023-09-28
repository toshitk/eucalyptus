from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

ASYNC_DB_URL = "mysql+aiomysql://root@db:3306/eucalyptus_local?charset=utf8"

BASE = declarative_base()


def create_session():
    async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
    async_session = sessionmaker(
        autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
    )
    return async_session()
