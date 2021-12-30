import json
from pprint import pprint

from .. import db
import os
import importlib

base_learning_model_path = 'cloud.app.main.learning_models.'  # Must be absolute path for this to work.


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def get_all_available_models():
    models = {}

    for module in os.listdir(os.path.dirname(__file__) + '/../learning_models/'):
        if module == '__init__.py' or module[-3:] != '.py':
            continue

        module_name = module[:-3]
        cls = getattr(importlib.import_module(base_learning_model_path + str(module_name)), module_name.capitalize())
        q = cls()
        models[module_name] = q.model_definition()  # TODO Decide what to do here with the model definitions
        models[module_name] = q.as_dict()

    return models
