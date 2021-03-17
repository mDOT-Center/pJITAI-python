import sentry_sdk

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

db = SQLAlchemy()

sentry_sdk.init(
    dsn="https://f91467158a64435d88a2dacfea084e1a@o361020.ingest.sentry.io/5679717",
    integrations=[FlaskIntegration(), SqlalchemyIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)


def create_app(config_name):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config_by_name[config_name])

    db.init_app(app)
    return app
