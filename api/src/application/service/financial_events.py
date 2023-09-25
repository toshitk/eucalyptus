from sqlalchemy.orm import Session
from src.infrastructure.database.model.financial_events import FinancialEvent
from src.infrastructure.database.repository.financial_events import (
    FinancialEventsRepository,
)


class FinancialEventsService:
    @staticmethod
    async def list_plan_events(session: Session, plan_id: int) -> list[FinancialEvent]:
        return await FinancialEventsRepository.list_by_plan_id(
            session=session, plan_id=plan_id
        )
