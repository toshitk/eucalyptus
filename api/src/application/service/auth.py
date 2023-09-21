from src.infrastructure.auth import create_auth0_user


class AuthService:
    @staticmethod
    def create(email: str, password: str) -> dict:
        return create_auth0_user(email=email, password=password)
