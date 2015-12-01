import os

from invoke import ctask as task
from invoke import Collection

from . import build, db, django, docs, pypi, test


@task(name='clean-python')
def clean_python(ctx):
    """Remove Python file artifacts."""
    ctx.run('find . -name \'*.pyc\' -delete')
    ctx.run('find . -name \'*.pyo\' -delete')
    ctx.run('find . -name \'*~\' -delete')
    ctx.run('find . -name \'__pycache__\' -delete')


# TODO Using call() in pre() does not yet work with Python 3.
# It triggers a "RuntimeError: maximum recursion depth exceeded while calling a
# Python object" exception. See https://github.com/pyinvoke/invoke/issues/257
@task(pre=[build.clean, clean_python, test.clean])
def clean(ctx):
    """Remove all build, test, coverage and Python artifacts."""
    builddir = docs.ns.configuration().get('sphinx').get('build_dir')
    docs.clean(ctx, builddir=builddir)


@task(name='clean-backups')
def clean_backups(ctx):
    """Remove backup files."""
    ctx.run('find . -name \'*~\' -delete')
    ctx.run('find . -name \'*.orig\' -delete')
    ctx.run('find . -name \'*.swp\' -delete')


@task
def develop(ctx):
    """Install (or update) all packages required for development."""
    ctx.run('pip install -U pip setuptools wheel')
    ctx.run('pip install -U -e .')
    ctx.run('pip install -U -r requirements/dev.txt')


@task
def isort(ctx):
    """Run isort to correct imports order."""
    command = 'isort --recursive setup.py {pkg_name}/ tasks/ tests/'.format(pkg_name=ctx.pkg_name)
    ctx.run(command)


ns = Collection(clean_python, clean, develop, build, db, django, docs, isort, pypi, test)
ns.configure({
    'base_dir': os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'env': 'dev',
    'pkg_name': '{{ cookiecutter.pkg_name }}',
    'run': {
        'echo': True,
        'pty': True,
    },
})
