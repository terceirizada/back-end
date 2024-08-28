from src.core.process.domain.dto.process_dto import ProcessOutPut
from src.core.process.domain.entity import Process
from src.core.process.domain.repository.process_repository import ProcessRepository


class InMemoryProcessRepository(ProcessRepository):
    def __init__(self, processs: list[Process]):
        self.processs = processs

    def list(self) -> list[ProcessOutPut]:
        return self.processs
