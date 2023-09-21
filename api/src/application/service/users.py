from sqlalchemy.orm import Session
from src.infrastructure.database.model.user import User
from src.infrastructure.database.repository.users import UsersRepository


class UsersService:
    @staticmethod
    async def find_by_id(session: Session, id: int) -> User:
        return await UsersRepository.find_by_id(session=session, id=id)

    @staticmethod
    async def register(session: Session, auth0_id: str, name: str, email: str) -> User:
        return await UsersRepository.insert(
            session=session, auth0_id=auth0_id, name=name, email=email
        )
