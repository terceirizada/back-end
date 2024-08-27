from abc import ABC, abstractmethod

from src.core.process.domain.entity import Process


class ProcessRepository(ABC):
    @abstractmethod
    def list(self) -> list[Process]:
        pass
