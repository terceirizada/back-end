import json

import pytest
from rest_framework.test import APIClient
from src.core.user.domain.entity import User
from src.framework.user.models import User as UserModel

STATUS_CREATED = 201


@pytest.mark.django_db
class TestCreateUserView:
    def test_create_user(self, client: APIClient):
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

        assert response.status_code == STATUS_CREATED
        assert response.json()["email"] == user.email

        user_db = UserModel.objects.get(email=user.email)
        assert user_db.email == user.email
