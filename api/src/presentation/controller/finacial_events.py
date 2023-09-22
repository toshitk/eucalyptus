from fastapi import APIRouter, Depends, Request
from src.infrastructure.auth import auth
from src.infrastructure.database.connection import create_session

router = APIRouter(prefix="/financial_events", tags=["financial_events"])


class FinancialEventsController:
    @staticmethod
    @router.get("/{plan_id}")
    async def get(
        request: Request,
        plan_id: int,
        user_id: int = Depends(auth),
        session=Depends(create_session),
    ):
        pass
