# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask

from . import controllers
from . import commands
from .database import db, migrate

from .settings import Config

def create_app(config_object=Config):
    """An application factory, took from:
    http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: - config object.
    """
    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_db(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_db(app):
    """Register db stuff."""
    db.init_app(app)
    migrate.init_app(app, db)

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(controllers.blueprint)

def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)
