from sqlalchemy import func

import datetime
from ..config import key

from .. import db


class LearningTask(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_on = db.Column(db.DateTime, nullable=False, server_default=func.now())
    last_modified = db.Column(db.DateTime, nullable=False, server_default=func.now())
    deleted = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return '<LearningTask: {}, {}, {}>'.format(self.id, self.created_on, self.last_modified)
