from dataclasses import dataclass


@dataclass
class InputCreateUser:
    email: str
    password: str


@dataclass
class OutputCreateUser:
    email: str
    id: str
