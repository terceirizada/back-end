from dataclasses import dataclass


@dataclass
class User:
    email: str
    id: str


@dataclass
class ProcessDto:
    responsavel: User
    candidato: str
    cargo: str
    status: str
    id: str


@dataclass
class ListProcessDto:
    data: list[ProcessDto]
