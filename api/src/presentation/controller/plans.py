from fastapi import APIRouter, Depends
from src.application.service.plans import PlansService
from src.infrastructure.database.connection import create_session
from src.presentation.schema.plans import RequestModel, ResponseModel

router = APIRouter(prefix="/plans", tags=["plans"])


class PlansController:
    @staticmethod
    @router.get("/{user_id}", response_model=list[ResponseModel])
    async def get(user_id: int, session=Depends(create_session)):
        return await PlansService.list_my_plans(session=session, user_id=user_id)

    @staticmethod
    @router.post("/{user_id}", response_model=ResponseModel)
    async def post(
        user_id: int, payload: RequestModel, session=Depends(create_session)
    ):
        return await PlansService.create_plan(
            session=session, user_id=user_id, name=payload.name
        )
