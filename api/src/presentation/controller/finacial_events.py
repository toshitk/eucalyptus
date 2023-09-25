from fastapi import APIRouter, Depends, Request
from src.application.service.financial_events import FinancialEventsService
from src.infrastructure.auth import auth
from src.infrastructure.database.connection import create_session
from src.presentation.schema.financial_events import ResponseModel

router = APIRouter(prefix="/financialEvents", tags=["financialEvents"])


class FinancialEventsController:
    @staticmethod
    @router.get("/{plan_id}", response_model=list[ResponseModel])
    async def get(
        request: Request,
        plan_id: int,
        user_id: int = Depends(auth),
        session=Depends(create_session),
    ):
        return await FinancialEventsService.list_plan_events(
            session=session, plan_id=plan_id
        )
