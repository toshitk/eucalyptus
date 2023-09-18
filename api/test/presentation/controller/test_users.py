from unittest.mock import patch

from fastapi.testclient import TestClient
from pytest import fixture
from src.infrastructrure.database.connection import create_session
from src.infrastructrure.database.model.user import User
from src.main import app

_service_class = "src.application.service.users.UsersService"


@fixture
def _fixture():
    app.dependency_overrides[create_session] = lambda: "dummy session"
    client = TestClient(app=app, base_url="http://test")
    return client


class TestUsersController:
    @patch(f"{_service_class}.find_by_id")
    def test_get(self, find_by_id, _fixture):
        client = _fixture

        find_by_id.return_value = User(id=1, name="John", email="@example.com")

        expected = {"id": 1, "name": "John", "email": "@example.com"}

        response = client.get("/users/1")

        assert response.status_code == 200
        assert response.json() == expected
        find_by_id.assert_called_once_with(session="dummy session", id=1)
