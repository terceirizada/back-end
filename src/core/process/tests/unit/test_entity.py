import pytest
from src.core.process.domain.entity import Process
from src.core.user.domain.entity import User
from src.core.user.domain.exceptions.user_exceptions import UserNotFoundError


@pytest.fixture
def user():
    return User(email="test@hotmail.com", password="12345678")


class TestUnitClassProcess:
    def test_process_instance(self, user: User):
        process = Process(
            responsavel=user,
            candidato="test",
            cargo="test",
            status="test",
        )

        assert process.responsavel == user
        assert process.candidato == "test"
        assert process.cargo == "test"

    def test_raise_exception_when_no_responsavel(self):
        with pytest.raises(UserNotFoundError) as excinfo:
            Process(
                responsavel=None,
                candidato="test",
                cargo="test",
                status="test",
            )
        assert str(excinfo.value) == "User not found"

    def test_raise_exception_when_no_candidato(self, user: User):
        with pytest.raises(Exception) as excinfo:
            Process(
                responsavel=user,
                candidato=None,
                cargo="test",
                status="test",
            )
        assert str(excinfo.value) == "Invalid candidato"

    def test_raise_exception_when_no_cargo(self, user: User):
        with pytest.raises(Exception) as excinfo:
            Process(
                responsavel=user,
                candidato="test",
                cargo=None,
                status="test",
            )
        assert str(excinfo.value) == "Invalid cargo"

    def test_raise_exception_when_no_status(self, user: User):
        with pytest.raises(Exception) as excinfo:
            Process(
                responsavel=user,
                candidato="test",
                cargo="test",
                status=None,
            )
        assert str(excinfo.value) == "Invalid status"
