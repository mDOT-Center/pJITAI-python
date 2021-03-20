import uuid
from abc import abstractmethod, ABCMeta


class LearningModelBase(metaclass=ABCMeta):
    """Base class for all learning models"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        super().__init__()

    @abstractmethod
    def run(self, command: str) -> (str, str):
        pass

    @abstractmethod
    def model_definition(self) -> dict:
        pass
