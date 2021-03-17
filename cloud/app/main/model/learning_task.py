from sqlalchemy import func

import datetime
from ..config import key

from .. import db


class LearningTask(db.Model):
    # __tablename__ = 'learning_tasks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # created_on = db.Column(db.DateTime, nullable=False, server_default=func.now())
    # last_modified = db.Column(db.DateTime, nullable=False, server_default=func.now())

    # def __repr__(self):
    #     return '<LearningTask: {}, {}, {}>'.format(self.id, self.created_on, self.last_modified)
