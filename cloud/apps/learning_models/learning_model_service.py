import os
import importlib
import inspect

base_learning_model_path = 'apps.learning_models.'  # Must be absolute path for this to work.


def get_all_available_models():
    models = {}

    for module in os.listdir(os.path.dirname(__file__)):
        if module == '__init__.py' or module[-3:] != '.py' or module=="learning_model_service.py" or module=="LearningModelBase.py":
            continue

        module_name = module[:-3]
        cls = getattr(importlib.import_module(base_learning_model_path + str(module_name)), module_name)

        q = cls()
        # models[module_name] = q.model_definition()  # TODO Decide what to do here with the model definitions
        models[module_name] = q.as_dict()
    return models

def get_all_available_models2():
    models = {}
