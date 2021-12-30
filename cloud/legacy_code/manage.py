import os
import unittest

from flask_migrate import Migrate, MigrateCommand

from flask_script import Manager

from app import blueprint
from app.main import create_app, db

# Models (Not used as import, but necessary for DB object creation
from app.main.model.learning_task import LearningTask

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.register_blueprint(blueprint)

app.app_context().push()
manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    try:
        app.run(host='0.0.0.0', port=80)
    except PermissionError as e:
        print('Permission denied: Port is use (80)')


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    manager.run()
