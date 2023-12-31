from test.presentation.controller.base import ControllerTestBase
from unittest.mock import patch

from src.infrastructure.database.model.plan import Plan

_service_class = "src.application.service.plans.PlansService"


class TestPlansController(ControllerTestBase):
    @patch(f"{_service_class}.list_my_plans")
    def test_get(self, list_my_plans, _fixture):
        client = _fixture

        list_my_plans.return_value = [
            Plan(id=1, user_id=1, name="My Plan1"),
            Plan(id=2, user_id=1, name="My Plan2"),
        ]

        expected = [
            {"id": 1, "name": "My Plan1"},
            {"id": 2, "name": "My Plan2"},
        ]

        response = client.get("/plans")

        assert response.status_code == 200
        assert response.json() == expected
        list_my_plans.assert_called_once_with(session="dummy", user_id=1)

    @patch(f"{_service_class}.create")
    def test_post(self, create, _fixture):
        client = _fixture

        create.return_value = Plan(id=1, user_id=1, name="Create Plan")
        expected = {"id": 1, "name": "Create Plan"}

        response = client.post("/plans", json={"name": "Create Plan"})

        assert response.status_code == 200
        assert response.json() == expected
        create.assert_called_once_with(session="dummy", user_id=1, name="Create Plan")
