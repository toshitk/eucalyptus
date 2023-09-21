from sqlalchemy import select
from sqlalchemy.orm import Session
from src.infrastructure.database.model.user import User


class UsersRepository:
    @staticmethod
    async def find_by_id(session: Session, id: int) -> User:
        result = await session.execute(
            select(User).where(User.id == id, User.deleted_at.is_(None))
        )

        return result.scalars().one_or_none()

    @staticmethod
    async def find_by_auth0_id(session: Session, auth0_id: str) -> User:
        result = await session.execute(
            select(User).where(User.auth0_id == auth0_id, User.deleted_at.is_(None))
        )

        return result.scalars().one_or_none()

    @staticmethod
    async def insert(session: Session, auth0_id: str, name: str, email: str) -> User:
        user = User(auth0_id=auth0_id, name=name, email=email)
        session.add(user)
        await session.commit()
        await session.refresh(user)

        return user
