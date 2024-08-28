from dataclasses import dataclass

from src.core.user.domain.dto.user_dto import UserOutPut


@dataclass
class ProcessOutPut:
    responsavel: UserOutPut
    candidato: str
    cargo: str
    status: str
    id: str
