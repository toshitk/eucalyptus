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
