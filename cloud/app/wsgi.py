import os

from cloud.app import blueprint
from cloud.app.main import create_app

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
