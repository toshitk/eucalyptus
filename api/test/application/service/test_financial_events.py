from unittest.mock import patch

import pytest
from src.application.service.financial_events import FinancialEventsService
from src.infrastructure.database.model.financial_events import FinancialEvent

_repo = (
    "src.infrastructure.database.repository.financial_events.FinancialEventsRepository"
)


class TestFinancialEventsService:
    @pytest.mark.asyncio
    @patch(f"{_repo}.list_by_plan_id")
    async def test_list_plan_events(self, list_by_plan_id):
        list_by_plan_id.return_value = [
            FinancialEvent(plan_id=1, type=1, name="salaly", year=2000, month=1)
        ]
        result = await FinancialEventsService.list_plan_events(
            session="dummy", plan_id=1
        )

        list_by_plan_id.assert_called_once_with(session="dummy", plan_id=1)
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], FinancialEvent)
