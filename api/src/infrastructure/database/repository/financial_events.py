from sqlalchemy import select
from sqlalchemy.orm import Session
from src.infrastructure.database.model.financial_events import FinancialEvent


class FinancialEventsRepository:
    @staticmethod
    async def list_by_plan_id(session: Session, plan_id: int) -> list[FinancialEvent]:
        result = await session.execute(
            select(FinancialEvent).where(
                FinancialEvent.plan_id == plan_id, FinancialEvent.deleted_at.is_(None)
            )
        )

        return result.scalars().all()
