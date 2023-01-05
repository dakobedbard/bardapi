import logging
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from bard import settings

NONE = "'none'"
log = logging.getLogger(__name__)
db = SQLAlchemy()
migrate = Migrate()


def create_app(config={}):

    app = Flask("bard")
    app.config.from_object(config)
    app.config.update(config)

    if "postgres" not in settings.DATABASE_URI:
        raise RuntimeError("bard database must be PostgreSQL!")

    app.config.update(
        {
            "SQLALCHEMY_DATABASE_URI": settings.DATABASE_URI,
            "FLASK_SKIP_DOTENV": True,
            "FLASK_DEBUG": True,
            "PROFILE": settings.PROFILE,
        }
    )
    migrate.init_app(app, db, directory=settings.ALEMBIC_DIR)
    db.init_app(app)

    CORS(
        app,
        resources=r"/api/*",
        origins="*",
        supports_credentials=True,
    )

    from bard.views import mount_app_blueprints

    mount_app_blueprints(app)
    return app


@migrate.configure
def configure_alembic(config):
    config.set_main_option("sqlalchemy.url", settings.DATABASE_URI)
    return config

