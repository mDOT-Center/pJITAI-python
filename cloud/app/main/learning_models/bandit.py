from cloud.app.main.util.LearningModelBase import LearningModelBase


class Bandit(LearningModelBase):


    def model_definition(self) -> dict:
        return self.metadata

    def __init__(self):
        super().__init__()
        self.x = 11
        self.y = 22
        self.description = 'This is the bandit model example'
        self.metadata = {'inputs': ['a', 'b'], 'parameters': ['pa', 'pb', 'pc'], 'outputs': ['result']}


    def run(self, command: str) -> (str, str):
        return "RUN", "success"

    def as_json(self):
        return 'JSON DUMP: ' + self.description
