# employees_app


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


Run database:
```
docker run -d --name mysql -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=db-password \
  -v /tmp:/var/lib/mysql mysql
```

```
docker run -d \
	--name dev-postgres \
	-e POSTGRES_PASSWORD=db-password \
	-v /tmp/postgres-data:/var/lib/postgresql/data \
     -p 5432:5432 postgres
```

Migrations
----------

Run the following commands ::

    flask db migrate

Then run ::

    flask db upgrade

To apply the migration.

For a full migration command reference, run ``flask db --help``.
