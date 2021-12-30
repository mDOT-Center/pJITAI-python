from apps.learning_models.LearningModelBase import LearningModelBase

class ThompsonSampling(LearningModelBase):

    def __init__(self):
        super().__init__()
        self.name = "Thompson Sampling"
        self.description = 'This is the thomson sampling algorithm definition.'
        # TODO: for all sigma range (0 to +inf) and for all mu, (-inf, +inf), Noise is same like sigma
        self.parameters = {
            "alpha0_mu": {
                "description": "Some description",
                "type": "float",
                "lower_bound": "-inf",
                "upper_bound":"inf",
                "inclusive": [True,True],
                "default_value": 0.9
            },
            "alpha0_sigma": {
                "description": "Some description",
                "type": "float",
                "lower_bound": 0,
                "upper_bound":"inf",
                "inclusive": [False,True],
                "default_value": 0.9
            },
            "beta_selected_features": {
                "description": "Some description",
                "type": "str",
                "lower_bound": "no",
                "upper_bound":"yes",
                "inclusive": [True,True],
                "default_value": "yes"
            },
            "beta_mu": {
                "description": "Some description",
                "type": "float",
                "lower_bound": "-inf",
                "upper_bound":"inf",
                "inclusive": [True,True],
                "default_value": 0.99
            },
            "beta_sigma": {
                "description": "Some description",
                "type": "float",
                "lower_bound": 0,
                "upper_bound":"inf",
                "inclusive": [False,True],
                "default_value": 0.9
            }
        }
        # TODO: change name -> standalone_parameters
        self.standalone_parameters = {
            "alpha_0_mu_bias": {
                "description": "Some description",
                "type": "float",
                "lower_bound": "-inf",
                "upper_bound":"inf",
                "inclusive": [True,True],
                "default_value": 0.31
            },
            "alpha_0_sigma_bias": {
                "description": "Some description",
                "type": "float",
                "lower_bound": 0,
                "upper_bound":"inf",
                "inclusive": [False,True],
                "default_value": 0.32
            },
            "beta_mu_bias" : {
                "description": "Some description",
                "type": "float",
                "lower_bound": "-inf",
                "upper_bound":"inf",
                "inclusive": [True,True],
                "default_value": 0.33
            },
            "beta_sigma_bias": {
                "description": "Some description",
                "type": "float",
                "lower_bound": 0,
                "upper_bound":"inf",
                "inclusive": [False,True],
                "default_value": 0.34
            },
            "noice": {
                "description": "Some description",
                "type": "float",
                "lower_bound": 0,
                "upper_bound":"inf",
                "inclusive": [False,True],
                "default_value": 0.35
            }

        }
        self.other_parameters = {
            "lower_clip": {
                "description": "Some description",
                "type": "float",
                "lower_bound": 0,
                "upper_bound":1,
                "inclusive": [True,True],
                "default_value": 0.39
            },
            "upper_clip": {
                "description": "Some description",
                "type": "float",
                "lower_bound": 0,
                "upper_bound":1,
                "inclusive": [True,True],
                "default_value": 0.8
            }
        }

        # TODO: move to base class??
        self.tuning_scheduler = {
            "name": "update_interval",
            "description": "time interval between running algorithm and update policy. Time is in seconds/minutes???",
            "type": "float",
            "lower_bound": 0,
            "upper_bound":"pinf",
            "inclusive": [True,True],
            "default_value": 0.39
        }
        # TODO: move to base class??
        # TODO: Not needed, more discussion is required
        self.availability = {
            "name": "availability",
            "description": "Do we need to check the availability of data",
            "type": "int",
            "default_value": 1
        }

        self.outputs = {'scaling_factor': 1.453, 'num': 148932}
        self.inputs = {'data': []}


    def run(self, command: str) -> (str, str):
        return "RUN", "success"