from flask_restx import Namespace, fields


class LearningTaskDto:
    api = Namespace('learning_task', description='Learning task operations')

    learning_task = api.model('learning_task', {
        'id': fields.Integer(
            required=False,
            description='DB identifier for this learning task'
        ),
        'created_on': fields.DateTime(
            required=False,
            description='Date and time this object was created'
        ),
        'last_modified': fields.DateTime(
            required=False,
            description='Date and time this object was last updated'
        )
    })
