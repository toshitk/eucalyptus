import os
from functools import wraps

import requests  # type: ignore
from dotenv import load_dotenv
from fastapi import HTTPException, Request
from jose import JWTError, jwt
from src.infrastructure.database.connection import create_session
from src.infrastructure.database.repository.users import UsersRepository

load_dotenv()
auth0_domain = os.getenv("AUTH0_DOMAIN")
auth0_audience = os.getenv("AUTH0_AUDIENCE")
auth0_client_id = os.getenv("AUTH0_CLIENT_ID")
auth0_client_secret = os.getenv("AUTH0_SECRET")


async def auth(request: Request):
    authorization = request.headers.get("Authorization")
    if authorization:
        auth0_id = _analyze_token(authorization=authorization)
        session = create_session()
        user = await UsersRepository.find_by_auth0_id(
            session=session, auth0_id=auth0_id
        )
        await session.close()
        return user.id
    else:
        raise HTTPException(status_code=401, detail="Authorization header is required")


def _analyze_token(authorization: str) -> str:
    token = _parse_authorization_header(authorization=authorization)
    rsa_key = _get_public_key(token=token)

    if not rsa_key:
        raise HTTPException(status_code=401, detail="Unable to find appropriate key")

    decoded_jwt = _decode_jwt_token(token=token, key=rsa_key)
    return decoded_jwt["sub"]


def _parse_authorization_header(authorization) -> str:
    splited_values = authorization.split()

    if splited_values[0].lower() != "bearer":
        raise HTTPException(status_code=401, detail="Invalid Authorization header")

    if len(splited_values) != 2:
        raise HTTPException(status_code=401, detail="Invalid Authorization header")

    return splited_values[1]


def _get_public_key(token: str) -> dict:
    jwks = _get_jwks()
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"],
            }
    return rsa_key


def _get_jwks() -> dict:
    response = requests.get(f"https://{auth0_domain}/.well-known/jwks.json")
    return response.json()


def _decode_jwt_token(token: str, key: dict) -> dict:
    try:
        payload = jwt.decode(
            token,
            key=key,
            algorithms=["RS256"],
            issuer="https://dev-e3ybvpddsjl3sbd7.us.auth0.com/",
            audience=auth0_audience,
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Signature has expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Error decoding token")

    return payload


def create_auth0_user(email: str, password: str) -> dict:
    token = _get_auth0_api_token()

    url = f"https://{auth0_domain}/api/v2/users"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {
        "email": email,
        "password": password,
        "connection": "Username-Password-Authentication",
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 201:
        raise HTTPException(status_code=400, detail=response.json()["message"])
    return response.json()


def _get_auth0_api_token() -> str:
    url = f"https://{auth0_domain}/oauth/token"
    payload = {
        "client_id": auth0_client_id,
        "client_secret": auth0_client_secret,
        "audience": f"https://{auth0_domain}/api/v2/",
        "grant_type": "client_credentials",
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to get API token")
    return response.json()["access_token"]
