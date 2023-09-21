from fastapi import APIRouter, Depends, Request
from src.application.service.auth import AuthService
from src.application.service.users import UsersService
from src.infrastructure.auth import auth, create_auth0_user
from src.infrastructure.database.connection import create_session
from src.presentation.schema.users import RequestModel, ResponseModel

router = APIRouter(prefix="/users", tags=["users"])


class UsersController:
    @staticmethod
    @router.get("/me", response_model=ResponseModel)
    async def get(
        request: Request, user_id: int = Depends(auth), session=Depends(create_session)
    ):
        return await UsersService.find_by_id(session=session, id=user_id)

    @staticmethod
    @router.post("", response_model=ResponseModel)
    async def post(payload: RequestModel, session=Depends(create_session)):
        auth0_user = AuthService.create(email=payload.email, password=payload.password)
        return await UsersService.create(
            session=session,
            auth0_id=auth0_user["user_id"],
            name=payload.name,
            email=auth0_user["name"],
        )
