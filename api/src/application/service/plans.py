from sqlalchemy.orm import Session
from src.infrastructrure.database.model.plan import Plan
from src.infrastructrure.database.repository.plans import PlansRepository


class PlansService:
    @staticmethod
    async def list_my_plans(session: Session, user_id: int) -> list[Plan]:
        return await PlansRepository.list_by_user_id(session=session, user_id=user_id)
