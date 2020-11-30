# employees_app
.. image:: image.png

set the ``FLASK_APP`` and ``FLASK_DEBUG``
environment variables ::

    export FLASK_APP=/path/to/autoapp.py
    export FLASK_DEBUG=1


initial migration ::

    flask db init
    flask db migrate
    flask db upgrade

To run the web application use::

    flask run --with-threads


Migrations
----------

Run the following commands ::

    flask db migrate

Then run ::

    flask db upgrade

To apply the migration.

For a full migration command reference, run ``flask db --help``.
