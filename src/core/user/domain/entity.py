import uuid
from dataclasses import dataclass, field

from email_validator import validate_email
from src.core.user.domain.exceptions.user_exceptions import (
    InvalidEmailError,
    InvalidPasswordError,
    InvalidUserError,
)

LENGTH_PASSWORD = 8


@dataclass
class User:
    email: str
    password: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def validate(self):
        if not self.email:
            raise InvalidUserError
        if not self.password:
            raise InvalidUserError
        if len(self.password) < LENGTH_PASSWORD:
            raise InvalidPasswordError
        try:
            validate_email(self.email)
        except Exception as e:
            raise InvalidEmailError from e

    def __post_init__(self):
        self.validate()

    def __str__(self):
        return f"User: {self.email}, id: {self.id}"

    def __repr__(self):
        return f"User: {self.email}, id: {self.id}"
