from sqlalchemy.orm import Session
from src.infrastructure.database.model.plan import Plan
from src.infrastructure.database.repository.plans import PlansRepository


class PlansService:
    @staticmethod
    async def list_my_plans(session: Session, user_id: int) -> list[Plan]:
        return await PlansRepository.list_by_user_id(session=session, user_id=user_id)

    @staticmethod
    async def create(session: Session, user_id: int, name: str) -> Plan:
        return await PlansRepository.create(session=session, user_id=user_id, name=name)
