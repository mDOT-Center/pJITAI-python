from cloud.app.main.util.LearningModelBase import LearningModelBase


class Bandit(LearningModelBase):

    def __init__(self):
        super().__init__()
        self.parameters = {'alpha': 1.1, 'beta': 0.5, 'n': 100}
        self.outputs = {'scaling_factor': 1.453, 'num': 148932}
        self.inputs = {'data': []}
        self.description = 'This is the bandit model example'

    def run(self, command: str) -> (str, str):
        return "RUN", "success"

    def model_definition(self) -> dict:
        return {'inputs': self.get_inputs(), 'outputs': self.get_outputs(), 'parameters': self.get_parameters()}
