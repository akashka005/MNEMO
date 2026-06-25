from abc import ABC
from abc import abstractmethod
from app.cke.result import CKEResult

class BaseCKEOperation(ABC):
    @abstractmethod
    def execute(
        self,
        source_node_id: str,
        target_node_id: str
    ) -> CKEResult:
        pass