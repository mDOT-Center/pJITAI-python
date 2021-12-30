from .. import db
from ..model.learning_task import LearningTask


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def get_all_learning_tasks():
    return LearningTask.query.all()


def create_new_learning_task():
    return LearningTask.query.all()


def get_learning_task(id):
    return LearningTask.query.filter_by(id=id).first()


def update_learning_task(id, data):
    # Update and save task here
    return LearningTask.query.filter_by(id=id).first()


def remove_learning_task(id):
    lt = LearningTask.query.filter_by(id=id).first()
    lt.deleted = True
    return lt
