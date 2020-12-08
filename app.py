# -*- coding: utf-8 -*-
"""Create an application instance."""

from backend.settings import Config
from backend.app import create_app
app = create_app(Config)

if __name__ == '__main__':
    app.run(debug=True)
