from test.infrastructure.database.repository.base import RepositoryTestBase

import pytest
from src.infrastructure.database.model.user import User
from src.infrastructure.database.repository.users import UsersRepository


class TestUsersRepository(RepositoryTestBase):
    @pytest.mark.asyncio
    async def test_find_by_id(self, _fixture):
        session = await _fixture

        async def setup():
            user = User(id=1, auth0_id="_", name="_", email="_")
            session.add(user)
            await session.flush()
            await session.refresh(user)

        async with self.setup_method(session=session, func=setup):
            result = await UsersRepository.find_by_id(session=session, id=1)
            assert isinstance(result, User)
