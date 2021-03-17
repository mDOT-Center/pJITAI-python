from flask_restx import Resource

from ..service.learning_task_service import get_all_learning_tasks
from ..util.dto import LearningTaskDto


api = LearningTaskDto.api

_learning_task = LearningTaskDto.learning_task


@api.route('/')
class LearningTask(Resource):

    @api.doc('List of Learning Tasks')
    @api.marshal_list_with(_learning_task, skip_none=True)
    def get(self):
        return get_all_learning_tasks()