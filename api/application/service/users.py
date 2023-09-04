from sqlalchemy.orm import Session

from api.infrastructrure.database.model.user import User
from api.infrastructrure.database.repository.users import UsersRepository


class UsersService:
    def list_by_id(self, session: Session, id: str) -> list[User]:
        return UsersRepository.list_by_id(session=session, id=id)
