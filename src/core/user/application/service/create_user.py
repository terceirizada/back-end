from src.core.user.application.dto.user_dto import InputCreateUser, OutputCreateUser
from src.core.user.domain.entity import User
from src.core.user.domain.exceptions.user_exceptions import UserAlreadyExistError
from src.core.user.domain.repository.user_repository import UserRepository
from src.core.utils.security.hash import get_password_hash


class CreateUser:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, input: InputCreateUser) -> OutputCreateUser:
        if user := self.repository.get_by_email(input.email):
            raise UserAlreadyExistError

        try:
            user = User(email=input.email, password=input.password)
            password_hash = get_password_hash(password=input.password)
            user.password = password_hash
            user = self.repository.save(user)
        except Exception as error:
            raise error
        return OutputCreateUser(email=user.email, id=user.id)
