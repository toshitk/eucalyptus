from fastapi import APIRouter, Depends, Request
from src.application.service.plans import PlansService
from src.infrastructure.auth import auth
from src.infrastructure.database.connection import create_session
from src.presentation.schema.plans import RequestModel, ResponseModel

router = APIRouter(prefix="/plans", tags=["plans"])


class PlansController:
    @staticmethod
    @router.get("", response_model=list[ResponseModel])
    async def get(
        request: Request, user_id: int = Depends(auth), session=Depends(create_session)
    ):
        return await PlansService.list_my_plans(session=session, user_id=user_id)

    @staticmethod
    @router.post("", response_model=ResponseModel)
    async def post(
        request: Request,
        payload: RequestModel,
        user_id: int = Depends(auth),
        session=Depends(create_session),
    ):
        return await PlansService.create_plan(
            session=session, user_id=user_id, name=payload.name
        )
