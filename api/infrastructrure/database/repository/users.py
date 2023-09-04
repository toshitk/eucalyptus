from sqlalchemy import select
from sqlalchemy.orm import Session

from api.infrastructrure.database.model.user import User


class UsersRepository:
    def list_by_id(session: Session, id: str) -> list[User]:
        result = session.execute(
            select(User).where(User.id == id, User.deleted_at.is_(None))
        )

        return result.schalars().all()
