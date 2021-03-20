import json
import uuid
from abc import abstractmethod, ABCMeta


class LearningModelBase(metaclass=ABCMeta):
    """Base class for all learning models"""
    parameters = {}
    inputs = {}
    outputs = {}
    description = ""

    def __init__(self):
        self.id = str(uuid.uuid4())
        super().__init__()

    def get_parameters(self) -> dict[str, str]:
        return {k: type(v).__name__ for k, v in self.parameters.items()}

    def get_outputs(self) -> dict[str, str]:
        return {k: type(v).__name__ for k, v in self.outputs.items()}

    def get_inputs(self) -> dict[str, str]:
        return {k: type(v).__name__ for k, v in self.inputs.items()}

    def as_dict(self) -> dict:
        return self.__dict__

    @abstractmethod
    def run(self, command: str) -> (str, str):
        pass

    @abstractmethod
    def model_definition(self) -> dict:
        pass
