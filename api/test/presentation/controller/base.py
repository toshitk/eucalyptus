from functools import wraps
from unittest.mock import patch

from fastapi.testclient import TestClient
from pytest import fixture
from src.infrastructure.database.connection import create_session
from src.main import app


class ControllerTestBase:
    @fixture
    def _fixture(self):
        app.dependency_overrides[create_session] = lambda: "dummy"
        client = TestClient(app=app, base_url="http://test")
        return client


def skip_auth():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # def dummy(*args, **kwargs):
            #     pass

            with patch(
                "src.infrastructure.auth._auth_impl",
                lambda func, *args, **kwargs: func(*args, **kwargs),
            ):
                return func(*args, **kwargs)

        return wrapper

    return decorator
