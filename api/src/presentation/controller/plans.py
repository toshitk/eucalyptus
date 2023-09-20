from fastapi import APIRouter, Depends, Request
from src.application.service.plans import PlansService
from src.infrastructure.auth import auth
from src.infrastructure.database.connection import create_session
from src.presentation.schema.plans import RequestModel, ResponseModel

router = APIRouter(prefix="/plans", tags=["plans"])


class PlansController:
    @staticmethod
    @router.get("/{user_id}", response_model=list[ResponseModel])
    @auth()
    async def get(request: Request, user_id: int, session=Depends(create_session)):
        return await PlansService.list_my_plans(session=session, user_id=user_id)

    @staticmethod
    @router.post("/{user_id}", response_model=ResponseModel)
    @auth()
    async def post(
        request: Request,
        user_id: int,
        payload: RequestModel,
        session=Depends(create_session),
    ):
        return await PlansService.create_plan(
            session=session, user_id=user_id, name=payload.name
        )
