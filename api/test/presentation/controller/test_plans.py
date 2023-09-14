from unittest.mock import patch

from fastapi.testclient import TestClient
from pytest import fixture
from src.infrastructrure.database.model.plan import Plan
from src.main import app


@fixture
def _fixture():
    client = TestClient(app=app, base_url="http://test")
    return client


class TestPlansController:
    @patch("src.application.service.plans.PlansService.list_my_plans")
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

        response = client.get("/plans/1")

        assert response.status_code == 200
        assert response.json() == expected
