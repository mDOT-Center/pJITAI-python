from cloud.app.main.util.LearningModelBase import LearningModelBase


class Dummy(LearningModelBase):

    def __init__(self):
        super().__init__()
        self.x = 1
        self.y = 2
        self.description = 'This is the bandit model example'

    def model_definition(self) -> dict:
        return {'inputs': ['aDD', 'bDD'], 'parameters': ['paDD', 'pbDD', 'pcDD'], 'outputs': ['resultDD']}

    def run(self, command: str) -> (str, str):
        return "RUN", "success"



    def as_json(self):
        return 'JSON DUMP: ' + self.description
