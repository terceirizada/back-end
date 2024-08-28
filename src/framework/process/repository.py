from src.core.process.domain.entity import Process
from src.core.process.domain.repository.process_repository import ProcessRepository
from src.framework.process.models import Process as ProcessModel


class DjangoORMProcessRepository(ProcessRepository):
    def __init__(self, process_model: ProcessModel):
        self.process_model = process_model

    def list(self) -> list[Process]:
        return self.process_model.objects.all()
