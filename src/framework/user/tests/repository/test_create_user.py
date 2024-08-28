import pytest
from src.core.user.domain.entity import User
from src.framework.user.models import User as UserModel
from src.framework.user.repository.repository import DjangoORMUserRepository


@pytest.mark.django_db
class TestDjangoORMUserRepository:
    def test_save(self):
        user = User(email="teste@hotmail.com", password="12345678")
        repository = DjangoORMUserRepository(UserModel)
        repository.save(user)

        assert UserModel.objects.count() == 1
        assert UserModel.objects.first().email == user.email

    def test_save_email_already_exists(self):
        user = User(email="teste@hotmail.com", password="12345678")
        repository = DjangoORMUserRepository(UserModel)
        repository.save(user)

        with pytest.raises(Exception) as excinfo:
            repository.save(user)

        assert str(excinfo.value) == "User already exists"
