from flask import request
from flask_restx import Resource

from ..service.learning_model_service import get_all_available_models
from ..util.dto import LearningTaskDto, LearningModelDto

api = LearningModelDto.api

_learning_model = LearningModelDto.learning_model


@api.route('/')
class LearningModel(Resource):

    @api.doc('List of existing learning models available in the system')
    # @api.marshal_list_with(_learning_model, skip_none=True)
    def get(self):
        return get_all_available_models()
