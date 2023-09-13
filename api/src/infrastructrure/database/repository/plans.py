from sqlalchemy import select
from sqlalchemy.orm import Session
from src.infrastructrure.database.model.plan import Plan


class PlansRepository:
    @staticmethod
    async def list_by_user_id(session: Session, user_id: int) -> list[Plan]:
        result = await session.execute(
            select(Plan).where(Plan.user_id == user_id, Plan.deleted_at.is_(None))
        )

        return result.scalars().all()
