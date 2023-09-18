from unittest.mock import patch

from fastapi.testclient import TestClient
from pytest import fixture
from src.infrastructrure.database.connection import create_session
from src.infrastructrure.database.model.plan import Plan
from src.main import app

_service _class = "src.application.service.plans.PlansService"


@fixture
def _fixture():
    app.dependency_overrides[create_session] = lambda: "dummy session"
    client = TestClient(app=app, base_url="http://test")
    return client


class TestPlansController:
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

        response = client.get("/plans/1")

        assert response.status_code == 200
        assert response.json() == expected
        list_my_plans.assert_called_once_with(session="dummy session", user_id=1)

    @patch(f"{_service_class}.create_plan")
    def test_post(self, create_plan, _fixture):
        client = _fixture

        create_plan.return_value = Plan(id=1, user_id=1, name="Create Plan")
        expected = {"id": 1, "name": "Create Plan"}

        response = client.post("/plans/1", json={"name": "Create Plan"})

        assert response.status_code == 200
        assert response.json() == expected
        create_plan.assert_called_once_with(
            session="dummy session", user_id=1, name="Create Plan"
        )
