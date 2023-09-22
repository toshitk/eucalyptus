from unittest.mock import AsyncMock, patch

import pytest
from src.application.service.users import UsersService
from src.infrastructure.database.model.user import User

_repo = "src.infrastructure.database.repository.users.UsersRepository"


class TestUsersService:
    @pytest.mark.asyncio
    @patch(f"{_repo}.find_by_id")
    async def test_find_by_id(self, find_by_id):
        # find_by_id.new_callable = AsyncMock
        find_by_id.return_value = User(
            id=1, auth0_id="dummy id", name="john", email="test@exampl.com"
        )
        result = await UsersService.find_by_id(session="dummy", id=1)

        find_by_id.assert_called_once_with(session="dummy", id=1)
        assert isinstance(result, User)

    @pytest.mark.asyncio
    @patch(f"{_repo}.insert")
    async def test_create(self, insert):
        # insert.new_callable = AsyncMock
        insert.return_value = User(
            auth0_id="dummy id", name="john", email="test@exampl.com"
        )
        result = await UsersService.create(
            session="dummy", auth0_id="dummy id", name="john", email="test@example.com"
        )

        insert.assert_called_once_with(
            session="dummy", auth0_id="dummy id", name="john", email="test@example.com"
        )
        assert isinstance(result, User)
