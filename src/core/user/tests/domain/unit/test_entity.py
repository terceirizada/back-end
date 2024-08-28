import pytest
from src.core.user.domain.entity import User
from src.core.user.domain.exceptions.user_exceptions import (
    InvalidPasswordError,
    InvalidUserError,
)


class TestUnitClassUser:
    def test_user_instance(self):
        password_ = "12345678"  # noqa
        user = User(email="test@hotmail.com", password=password_)
        assert user.email == "test@hotmail.com"
        assert user.password != password_

    def test_user_instance_with_id(self):
        user = User(email="test@hotmail.com", password="12345678")
        assert user.id is not None

    def test_raise_exception_when_no_email(self):
        with pytest.raises(InvalidUserError) as excinfo:
            User(email="", password="12345678")
        assert str(excinfo.value) == "Invalid user"

    def test_raise_exception_when_password_less_than_8(self):
        with pytest.raises(InvalidPasswordError) as excinfo:
            User(email="test@hotmail.com", password="1234567")
        assert str(excinfo.value) == "Password must be at least 8 characters long"
