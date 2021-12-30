from flask_restx import Api
from flask import Blueprint

from .main.controller.learning_task_controller import api as lt_ns
from .main.controller.learning_model_controller import api as lm_ns

blueprint = Blueprint('api', __name__, url_prefix="/")

api = Api(blueprint,
          title='mDOT Reinforcement Learning Service',
          version='1.0',
          description='A Reinforcement Learning service for mDOT'
          )

api.add_namespace(lt_ns, path='/learning_task')
api.add_namespace(lm_ns, path='/learning_model')
