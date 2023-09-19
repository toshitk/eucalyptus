from functools import wraps

import requests  # type: ignore
from fastapi import HTTPException
from jose import JWTError, jwt

auth0_domain = "dev-e3ybvpddsjl3sbd7.us.auth0.com"
auth0_audience = "https://dev-e3ybvpddsjl3sbd7.us.auth0.com/api/v2/"


def auth():
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            request = kwargs.get("request")
            authorization = request.headers.get("Authorization")

            return await func(*args, **kwargs)

        return wrapper

    return decorator
