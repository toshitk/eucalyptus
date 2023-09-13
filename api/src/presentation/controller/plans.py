from fastapi import APIRouter, Depends
from src.application.service.plans import PlansService
from src.infrastructrure.database.connection import create_session
from src.presentation.schema.plans import ResponseModel

router = APIRouter(prefix="/plans", tags=["plans"])


class PlansController:
    @staticmethod
    @router.get("/{user_id}", response_model=ResponseModel)
    async def get(user_id: int, session=Depends(create_session)):
        return await PlansService.list_my_plans(session=session, user_id=user_id)
