from sqlalchemy.orm import Session
from src.infrastructrure.database.model.user import User
from src.infrastructrure.database.repository.users import UsersRepository


class UsersService:
    @staticmethod
    async def list_by_id(session: Session, id: int) -> list[User]:
        return await UsersRepository.list_by_id(session=session, id=id)
