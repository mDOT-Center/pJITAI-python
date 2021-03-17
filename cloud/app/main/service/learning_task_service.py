from .. import db
from ..model.learning_task import LearningTask


def get_all_learning_tasks():
    return LearningTask.query.all()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
