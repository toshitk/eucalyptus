from fastapi import APIRouter, Depends, Request
from src.application.service.users import UsersService
from src.infrastructure.auth import auth
from src.infrastructure.database.connection import create_session
from src.presentation.schema.users import ResponseModel

router = APIRouter(prefix="/users", tags=["users"])


class UsersController:
    @staticmethod
    @router.get("/{user_id}", response_model=ResponseModel)
    @auth()
    async def get(request: Request, user_id: int, session=Depends(create_session)):
        print("aaa")
        return await UsersService.find_by_id(session=session, id=user_id)
