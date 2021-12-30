from flask import request
from flask_restx import Resource

from ..service.learning_task_service import get_all_learning_tasks, get_learning_task, create_new_learning_task, \
    remove_learning_task, update_learning_task
from ..util.dto import LearningTaskDto

api = LearningTaskDto.api

_learning_task = LearningTaskDto.learning_task


@api.route('/')
class LearningTask(Resource):

    @api.doc('List of existing learning tasks')
    @api.marshal_list_with(_learning_task, skip_none=True)
    def get(self):
        return get_all_learning_tasks()

    @api.doc('Create a new learning task')
    def post(self):
        data = request.json
        return create_new_learning_task(data)


@api.route('/<uuid:uuid>')
class LearningTaskDetails(Resource):
    @api.doc('Learning task details')
    def get(self):
        return get_learning_task(id)

    @api.doc('Update learning task with new data/parameters')
    def put(self):
        data = request.json
        return update_learning_task(id, data)

    @api.doc('Remove a learning task')
    def delete(self):
        return remove_learning_task(id)
