import json
import uuid
from abc import abstractmethod, ABCMeta


class LearningModelBase(metaclass=ABCMeta):
    name = ""
    desciption = ""
    parameters = {}
    standalone_parameters = []
    other_parameters = []
    tuning_scheduler = {}
    # availability = {}

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

    def model_definition(self) -> dict:
        return {'inputs': self.get_inputs(), 'outputs': self.get_outputs(), 'parameters': self.get_parameters()}