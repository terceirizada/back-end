import uuid
from dataclasses import dataclass, field

from src.core.process.domain.exceptions.process_exceptions import (
    InvalidCandidatoError,
    InvalidCargoError,
    InvalidStatusError,
)
from src.core.user.domain.entity import User
from src.core.user.domain.exceptions.user_exceptions import UserNotFoundError

LENGTH_PASSWORD = 8


@dataclass
class Process:
    responsavel: User
    candidato: str
    cargo: str
    status: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def validate(self):
        if not self.responsavel:
            raise UserNotFoundError
        if not self.candidato:
            raise InvalidCandidatoError
        if not self.cargo:
            raise InvalidCargoError
        if not self.status:
            raise InvalidStatusError

    def __post_init__(self):
        self.validate()

    def __str__(self):
        return f"{self.candidato} - {self.cargo} - {self.status}"

    def __eq__(self, other: object) -> bool:
        return self.id == other.id if isinstance(other, Process) else False

    def __repr__(self) -> str:
        return f"Process({self.responsavel}, {self.candidato}, {self.cargo}, {self.status}, {self.id})"
