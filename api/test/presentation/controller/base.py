from fastapi.testclient import TestClient
from pytest import fixture
from src.infrastructure.auth import auth
from src.infrastructure.database.connection import create_session
from src.main import app


class ControllerTestBase:
    @fixture
    def _fixture(self):
        app.dependency_overrides[create_session] = lambda: "dummy"
        app.dependency_overrides[auth] = lambda: 1
        client = TestClient(app=app, base_url="http://test")
        return client
