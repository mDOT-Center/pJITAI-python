from cloud.app.main.util.LearningModelBase import LearningModelBase


class Dummy(LearningModelBase):

    def __init__(self):
        super().__init__()
        self.parameters = {'param1': 1, 'param2': "string"}
        self.outputs = {'output1': 12345, 'output2': {}}
        self.inputs = {'input1': [], 'input2': 1233}
        self.description = 'This is the bandit model example'

    def run(self, command: str) -> (str, str):
        return "RUN", "success"

