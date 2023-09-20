from test.presentation.controller.base import ControllerTestBase, dummy_auth
from unittest.mock import patch

from src.infrastructure.database.model.user import User

_service_class = "src.application.service.users.UsersService"


class TestUsersController(ControllerTestBase):
    @dummy_auth()
    @patch(f"{_service_class}.find_by_id")
    def test_get(self, find_by_id, _fixture):
        client = _fixture

        find_by_id.return_value = User(id=1, name="John", email="@example.com")

        expected = {"id": 1, "name": "John", "email": "@example.com"}

        response = client.get("/users/1")

        assert response.status_code == 200
        assert response.json() == expected
        find_by_id.assert_called_once_with(session="dummy", id=1)
