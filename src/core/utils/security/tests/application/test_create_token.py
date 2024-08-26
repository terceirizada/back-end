import warnings

import pytest
from src.core.user.domain.entity import User
from src.core.user.infra.in_memory_user import InMemoryUserRepository
from src.core.utils.security.application.dto.jwt import InputAuthUserDto
from src.core.utils.security.application.service.auth_jwt import JWTCreator
from src.core.utils.security.hash import get_password_hash
from src.core.utils.security.jwt import decode_jwt

STATUS_CONFLICT = 409
EXP = 60

warnings.filterwarnings("ignore", category=DeprecationWarning, module="passlib.utils")


@pytest.fixture
def repository():
    return InMemoryUserRepository()


@pytest.fixture
def repository_with_user():
    repository = InMemoryUserRepository()
    repository.save(
        User(email="test@hotmail.com", password=get_password_hash("12345678")),
    )
    return repository


class TestCreateJWT:
    def test_create_jwt(self, repository_with_user: InMemoryUserRepository):
        request = InputAuthUserDto(email="test@hotmail.com", password="12345678")
        service = JWTCreator(repository_with_user)
        response = service.execute(input=request)

        assert response.token is not None
        assert response.exp == EXP

        decode = decode_jwt(response.token)
        assert decode["email"] == "test@hotmail.com"
        assert decode["exp"] == EXP
