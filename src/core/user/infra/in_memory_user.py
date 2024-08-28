from src.core.user.domain.dto.user_dto import UserOutPut
from src.core.user.domain.entity import User
from src.core.user.domain.repository.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self, users: list[User] = []):
        self.users = users

    def save(self, user: User) -> UserOutPut:
        self.users.append(user)
        return user

    def get_by_email(self, email: str) -> UserOutPut:
        return next((user for user in self.users if user.email == email), None)
