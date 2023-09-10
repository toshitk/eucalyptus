from sqlalchemy.orm import Session
from src.infrastructrure.database.model.user import User
from src.infrastructrure.database.repository.users import UsersRepository


class UsersService:
    @staticmethod
    async def find_by_id(session: Session, id: int) -> User:
        return await UsersRepository.find_by_id(session=session, id=id)
