import pytest
from rest_framework.test import APIClient

from src.core.user.domain.entity import User
from src.core.utils.security.application.service.auth_jwt import (
    InputAuthUserDto,
    JWTCreator,
)
from src.framework.process.models import Process as ProcessModel
from src.framework.user.models import User as UserModel
from src.framework.user.repository.repository import DjangoORMUserRepository

STATUS_OK = 200
STATUS_NOT_AUTHENTICATED = 403
HASH_DEFAULT = "12345678"


@pytest.fixture
def user() -> User:
    return User(email="test@hotmail.com", password="12345678")


@pytest.fixture
def client() -> APIClient:
    return APIClient()


@pytest.mark.django_db
class TestViewListProccess:
    def test_list_process(self, user: User, client: APIClient):
        repository = DjangoORMUserRepository(UserModel)
        repository.save(user)

        service_jwt = JWTCreator(repository=repository)
        jwt = service_jwt.execute(
            InputAuthUserDto(email=user.email, password=HASH_DEFAULT),
        )

        process_model = ProcessModel.objects.create(
            cargo="advogado",
            responsavel=UserModel.objects.get(email="test@hotmail.com"),
            status="andamento",
            candidato="lucas",
        )
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt.token}")

        response = client.get("/api/processes/")
        assert response.status_code == STATUS_OK

        response_data = response.json()
        assert len(response_data) == 1
        assert response_data["data"][0] == {
            "id": str(process_model.id),
            "cargo": process_model.cargo,
            "status": process_model.status,
            "candidato": process_model.candidato,
            "responsavel": {
                "email": process_model.responsavel.email,
                "id": str(process_model.responsavel.id),
            },
        }

    def test_list_when_not_authenticated(self, client: APIClient):
        response = client.get("/api/processes/")
        assert response.status_code == STATUS_NOT_AUTHENTICATED
        assert response.json() == {"detail": "No token provided"}
