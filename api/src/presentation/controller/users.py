from fastapi import APIRouter, Depends
from src.application.service.users import UsersService
from src.infrastructrure.database.connection import create_session
from src.presentation.schema.users import ResponseModel

router = APIRouter(prefix="/users", tags=["users"])


class UsersController:
    @staticmethod
    @router.get("/{user_id}", response_model=list[ResponseModel])
    async def get(user_id: int, session=Depends(create_session)):
        return await UsersService.list_by_id(session=session, id=user_id)
