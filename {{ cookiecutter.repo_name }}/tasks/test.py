import os
import webbrowser

from invoke import ctask as task
from invoke import Collection

from . import helpers


@task
def all(ctx):
    """Run all tox environments."""
    ctx.run('tox')


@task
def clean(ctx):
    """Remove test and coverage artifacts."""
    ctx.run('rm -fr .cache/')
    ctx.run('rm -fr .tox/')
    ctx.run('coverage erase')
    ctx.run('rm -fr htmlcov/')


@task
def coverage(ctx, env=None):
    """Run tests and create a coverage report."""
    ctx.run(helpers.envdir(ctx, 'coverage run -m pytest tests/', env or ctx.env))
    ctx.run('coverage report')


@task(pre=[coverage], name='coverage-html')
def coverage_html(ctx):
    """Create a coverage html report and open it in the default browser."""
    uri = 'file://{cwd}/htmlcov/index.html'.format(cwd=os.getcwd())
    ctx.run('coverage html')
    webbrowser.open(uri)


@task
def run(ctx, test_args='', env=None):
    """Run project tests."""
    command = 'py.test {test_args} tests/'.format(test_args=test_args)
    ctx.run(helpers.envdir(ctx, command, env or ctx.env))


ns = Collection(all, clean, coverage, coverage_html, run)
