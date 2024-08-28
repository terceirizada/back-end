import pytest
from src.core.process.application.service.list_process import ListProcess
from src.core.process.domain.entity import Process
from src.core.process.infra.in_memory_process import InMemoryProcessRepository
from src.core.user.domain.entity import User


@pytest.fixture
def user() -> User:
    return User(email="teste@hotmail.com", password="12345678")


@pytest.fixture
def process(user: User) -> Process:
    return Process(
        responsavel=user,
        candidato="Joao",
        cargo="Dev",
        status="Em andamento",
    )


class TestListProcesses:
    def test_list_process(self, process: Process):
        repository = InMemoryProcessRepository([process])
        list_process = ListProcess(repository)
        result = list_process.execute()
        assert len(result.data) == 1
        assert result.data[0].responsavel.email == "teste@hotmail.com"
        assert result.data[0].candidato == "Joao"
        assert result.data[0].cargo == "Dev"
        assert result.data[0].status == "Em andamento"
        assert result.data[0].id == process.id
