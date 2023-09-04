from fastapi import APIRouter

from api.presentation.schema.users import ResponseModel

router = APIRouter(prefix="/users", tags=["users"])


class UsersController:
    @staticmethod
    @router.get("/{id}", response_model=list[ResponseModel])
    async def get():
        pass
