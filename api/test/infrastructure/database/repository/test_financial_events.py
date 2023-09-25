from test.infrastructure.database.repository.base import RepositoryTestBase

import pytest
from src.infrastructure.database.model.financial_events import FinancialEvent
from src.infrastructure.database.repository.financial_events import (
    FinancialEventsRepository,
)


class TestFinancialEventsRepository(RepositoryTestBase):
    @pytest.mark.asyncio
    async def test_list_by_plan(self, _fixture):
        session = await _fixture

        async def setup():
            financial_event = FinancialEvent(
                plan_id=1, type=1, name="saraly", year=2000, month=1
            )
            session.add(financial_event)
            await session.flush()
            await session.refresh(financial_event)

        async with self.setup_method(session=session, func=setup):
            result = await FinancialEventsRepository.list_by_plan_id(
                session=session, plan_id=1
            )
            assert isinstance(result, list)
            assert len(result) == 1
            assert isinstance(result[0], FinancialEvent)
