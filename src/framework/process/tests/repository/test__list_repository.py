import pytest

from src.core.user.domain.entity import User
from src.framework.process.models import Process as ProcessModel
from src.framework.process.repository import DjangoORMProcessRepository
from src.framework.user.models import User as UserModel
from src.framework.user.repository.repository import DjangoORMUserRepository


@pytest.fixture
def user() -> User:
    return User(email="test@hotmail.com", password="12345678")


@pytest.mark.django_db
class TestDjangoORMProcessRepository:
    def test_list_processes(self, user: User):
        repository_user = DjangoORMUserRepository(UserModel)
        repository_user.save(user)

        process_model = ProcessModel.objects.create(
            cargo="advogado",
            responsavel=UserModel.objects.get(email="test@hotmail.com"),
            status="andamento",
            candidato="lucas",
        )

        repository = DjangoORMProcessRepository(ProcessModel)
        processes = repository.list()

        assert len(processes) == 1
        assert processes[0].cargo == process_model.cargo
        assert processes[0].status == process_model.status
        assert processes[0].candidato == process_model.candidato
        assert processes[0].responsavel.email == process_model.responsavel.email

    def test_list_processes_empty(self):
        repository = DjangoORMProcessRepository(ProcessModel)
        processes = repository.list()

        assert len(processes) == 0
