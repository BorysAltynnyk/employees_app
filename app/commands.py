# -*- coding: utf-8 -*-
"""Click commands."""
import os
import click

TEST_PATH = os.path.join(PROJECT_ROOT, 'tests')

@click.command()
def test():
    """Run the tests."""
    import pytest
    rv = pytest.main([TEST_PATH, '--verbose'])
    exit(rv)