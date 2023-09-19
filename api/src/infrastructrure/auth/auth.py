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
            # _analyze_token(authorization=authorization)
            return await func(*args, **kwargs)

        return wrapper

    return decorator


def get_jwks():
    response = requests.get(f"https://{auth0_domain}/.well-known/jwks.json")
    return response.json()


def get_public_key(token: str):
    jwks = get_jwks()
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


def _analyze_token(authorization: str) -> None:
    token = _parse_authorization_header(authorization=authorization)
    print(f"token: {token}")

    rsa_key = get_public_key(token=token)
    print(f"rsa_key: {rsa_key}")

    if not rsa_key:
        raise HTTPException(status_code=401, detail="Unable to find appropriate key")

    decoded_jwt = _decode_jwt_token(token=token, key=rsa_key)
    print(f"decoded_jwt: {decoded_jwt}")


def _decode_jwt_token(token: str, key: str) -> dict:
    try:
        payload = jwt.decode(
            jwt=token,
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


def _parse_authorization_header(authorization):
    splited_values = authorization.split()

    if splited_values[0].lower() != "bearer":
        raise HTTPException(status_code=401, detail="Invalid Authorization header")

    if len(splited_values) != 2:
        raise HTTPException(status_code=401, detail="Invalid Authorization header")

    return splited_values[1]
