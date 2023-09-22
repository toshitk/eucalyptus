from test.infrastructure.database.repository.base import RepositoryTestBase

import pytest
from src.infrastructure.database.model.user import User
from src.infrastructure.database.repository.users import UsersRepository


class TestUsersRepository(RepositoryTestBase):
    @pytest.mark.asyncio
    async def test_find_by_id(self, _fixture):
        session = await _fixture
        user = User(id=1, auth0_id="_", name="_", email="_")
        session.add(user)
        await session.commit()
        await session.refresh(user)

        result = await UsersRepository.find_by_id(session=session, id=1)
        assert isinstance(result, User)
        await session.close()
