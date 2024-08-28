from src.core.process.application.dto.process import ListProcessDto, ProcessDto
from src.core.process.domain.repository.process_repository import ProcessRepository


class ListProcess:
    def __init__(self, repository: ProcessRepository):
        self.repository = repository

    def execute(self) -> list[ListProcessDto]:
        processes = self.repository.list()
        return ListProcessDto(
            data=[
                ProcessDto(
                    responsavel=process.responsavel,
                    candidato=process.candidato,
                    cargo=process.cargo,
                    status=process.status,
                    id=process.id,
                )
                for process in processes
            ],
        )
