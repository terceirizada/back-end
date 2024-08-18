from abc import ABC, abstractmethod

from src.core.user.domain.entity import User


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User:
        pass
