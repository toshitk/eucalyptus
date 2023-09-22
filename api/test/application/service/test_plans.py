from unittest.mock import patch

import pytest
from src.application.service.plans import PlansService
from src.infrastructure.database.model.plan import Plan

_repo = "src.infrastructure.database.repository.plans.PlansRepository"


class TestPlansService:
    @pytest.mark.asyncio
    @patch(f"{_repo}.list_by_user_id")
    async def test_list_my_plans(self, list_by_user_id):
        list_by_user_id.return_value = [Plan(user_id=1, name="_")]
        result = await PlansService.list_my_plans(session="dummy", user_id=1)

        list_by_user_id.assert_called_once_with(session="dummy", user_id=1)
        assert isinstance(result, list)
        assert isinstance(result[0], Plan)

    @pytest.mark.asyncio
    @patch(f"{_repo}.create")
    async def test_create(self, create):
        create.return_value = Plan(user_id=1, name="My Plan")
        result = await PlansService.create(session="dummy", user_id=1, name="My Plan")

        create.assert_called_once_with(session="dummy", user_id=1, name="My Plan")
        assert isinstance(result, Plan)
