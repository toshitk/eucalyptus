from unittest.mock import AsyncMock, patch

import pytest
from src.application.service.users import UsersService
from src.infrastructure.database.model.user import User

_repo = "src.infrastructure.database.repository.users.UsersRepository"


class TestUserService:
    @pytest.mark.asyncio
    @patch(f"{_repo}.find_by_id")
    async def test_find_by_id(self, find_by_id):
        find_by_id.new_callable = AsyncMock
        await UsersService.find_by_id(session="dummy", id=1)

        find_by_id.assert_called_once_with(session="dummy", id=1)
