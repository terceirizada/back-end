import json

import pytest
from rest_framework.test import APIClient

from src.core.user.domain.entity import User
from src.framework.user.models import User as UserModel
from src.framework.user.repository.repository import DjangoORMUserRepository

STATUS_OK = 200
STATUS_ALREADY_EXISTS = 409
STATUS_CREATED = 201
STATUS_USER_NOT_FOUND = 404


@pytest.fixture
def repository():
    return DjangoORMUserRepository(user_model=UserModel)


@pytest.mark.django_db
class TestCreateAuthUserView:
    def test_login_user(self, client: APIClient, repository: DjangoORMUserRepository):
        user = User(email="test@hotmail.com", password="12345678")
        data = {
            "email": user.email,
            "password": user.password,
        }

        response = client.post(
            "/api/users/",
            data=json.dumps(data),
            content_type="application/json",
        )

        response = client.post(
            "/api/auth/",
            data=json.dumps(data),
            content_type="application/json",
        )

        assert response.json() == {
            "token": response.json()["token"],
            "exp": response.json()["exp"],
        }
        assert response.status_code == STATUS_OK

    def teste_login_user_not_found(self, client: APIClient):
        data = {
            "email": "test@hotmail.com",
            "password": "12345678",
        }

        response = client.post(
            "/api/auth/",
            data=json.dumps(data),
            content_type="application/json",
        )

        assert response.json() == {"error": "User not found"}
        assert response.status_code == STATUS_USER_NOT_FOUND
