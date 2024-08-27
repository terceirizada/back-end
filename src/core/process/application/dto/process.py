from dataclasses import dataclass


@dataclass
class User:
    email: str
    id: str


@dataclass
class ListProcessDto:
    responsavel: User
    candidato: str
    cargo: str
    status: str
    id: str
