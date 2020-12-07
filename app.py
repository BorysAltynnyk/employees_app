# -*- coding: utf-8 -*-
"""Create an application instance."""

from .app.settings import Config
from .app.app import create_app
app = create_app(Config)
