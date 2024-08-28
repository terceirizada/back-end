from abc import ABC, abstractmethod

from src.core.process.domain.dto.process_dto import ProcessOutPut


class ProcessRepository(ABC):
    @abstractmethod
    def list(self) -> list[ProcessOutPut]:
        pass
