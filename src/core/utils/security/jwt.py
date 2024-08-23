import os

import jwt


def create_jwt(payload: dict[str]) -> str:
    return jwt.encode(
        payload=payload,
        key=os.getenv("SECRET_KEY"),
        algorithm=os.getenv("ALGORITHM"),
    )


def decode_jwt(token: str) -> dict:
    return jwt.decode(
        jwt=token,
        key=os.getenv("SECRET_KEY"),
        algorithms=[os.getenv("ALGORITHM")],
    )
