from unittest.mock import patch

from src.application.service.auth import AuthService

_auth_service_path = "src.application.service.auth"


class TestAuthService:
    @patch(f"{_auth_service_path}.create_auth0_user")
    def test_create(self, create):
        create.return_value = {
            "created_at": "2000-01-01T00:00:00.000Z",
            "email": "sample@example.com",
            "email_verified": False,
            "identities": [
                {
                    "connection": "Username-Password-Authentication",
                    "user_id": "650bcb3b6371a502e023222a",
                    "provider": "auth0",
                    "isSocial": False,
                }
            ],
            "name": "sample@example.com",
            "nickname": "sample",
            "picture": "https://sample.png",
            "updated_at": "2000-01-01T00:00:00.000Z",
            "user_id": "auth0|650bcb3b6371a502e023222a",
        }
        auth0_user = AuthService.create(
            email="sample@example.com", password="Password1234"
        )

        assert auth0_user["user_id"] == "auth0|650bcb3b6371a502e023222a"
        assert auth0_user["name"] == "sample@example.com"
        create.assert_called_once_with(
            email="sample@example.com", password="Password1234"
        )
