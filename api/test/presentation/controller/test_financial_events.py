from test.presentation.controller.base import ControllerTestBase
from unittest.mock import patch

from src.infrastructure.database.model.financial_events import FinancialEvent

_service_class = "src.application.service.financial_events.FinancialEventsService"


class TestFinancialEventsController(ControllerTestBase):
    @patch(f"{_service_class}.list_plan_events")
    def test_get(self, list_plan_events, _fixture):
        client = _fixture

        list_plan_events.return_value = [
            FinancialEvent(
                id=1,
                plan_id=1,
                type=1,
                category="salary",
                name="monthly salary",
                year=2000,
                month=1,
                amount=500000,
            ),
            FinancialEvent(
                id=2,
                plan_id=1,
                type=1,
                category="salary",
                name="monthly salary",
                year=2000,
                month=2,
                amount=600000,
            ),
        ]

        expected = [
            {
                "id": 1,
                "plan_id": 1,
                "type": 1,
                "category": "salary",
                "name": "monthly salary",
                "year": 2000,
                "month": 1,
                "amount": 500000,
            },
            {
                "id": 2,
                "plan_id": 1,
                "type": 1,
                "category": "salary",
                "name": "monthly salary",
                "year": 2000,
                "month": 2,
                "amount": 600000,
            },
        ]

        response = client.get("/financialEvents/1")

        assert response.status_code == 200
        assert response.json() == expected
        list_plan_events.assert_called_once_with(session="dummy", plan_id=1)
