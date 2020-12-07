# -*- coding: utf-8 -*-
"""Click commands."""
import os
import click

from datetime import datetime

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)
TEST_PATH = os.path.join(PROJECT_ROOT, 'tests')

@click.command()
def test():
    """Run the tests."""
    import pytest
    rv = pytest.main([TEST_PATH, '--verbose'])
    exit(rv)

@click.command()
def seed():
    """Seed data"""
    from .database import db
    from .models import Department, Employee
    from .app import create_app
    app = create_app()
    with app.app_context():
        birth_date_b = datetime.strptime('10 June, 1996', "%d %B, %Y")
        # employee = Employee(name='Borys', salary=100, birth_date=birth_date_b, department_id=1)
        employee = Employee(name='ALexey Oleynik', salary=40000, birth_date=birth_date_b, department_id=1)
        db.session.add(employee)
        db.session.commit()


@click.command()
def seeddeps():
    """Seed departament"""
    from .database import db
    from .models import Department
    from .app import create_app

    app = create_app()
    with app.app_context():
        db.session.add(Department(name='HR'))
        db.session.add(Department(name='PR'))
        db.session.add(Department(name='AR'))
        db.session.add(Department(name='VIP'))
        db.session.commit()

