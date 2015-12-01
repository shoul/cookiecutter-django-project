import os

from invoke import ctask as task
from invoke import Collection


@task(help={'command': "Django command to execute", 'env': "envdir name to use"})
def manage(ctx, command, env=None):
    """Execute a Django command using the given env."""
    command = 'envdir {envdir} python {manage_py} {command}'.format(
        envdir=os.path.join(ctx.base_dir, 'envs', env or ctx.env),
        manage_py=os.path.join(ctx.base_dir, 'manage.py'),
        command=command
    )
    ctx.run(command)


@task(help={'port': "Port to use"})
def runserver(ctx, port=None):
    """Start Django's development Web server"""
    manage(ctx, 'runserver {0}'.format(port or ctx.django.port))


@task
def shell(ctx):
    """Run a Python interactive interpreter"""
    manage(ctx, 'shell')


@task(help={'name': "Name of the app to create"})
def startapp(ctx, name):
    """Create a Django app directory structure for the given app name"""
    directory = os.path.join(ctx.base_dir, ctx.pkg_name, name)
    os.mkdir(directory)
    manage(ctx, ' '.join(('startapp', name, directory)))


ns = Collection(manage, runserver, shell, startapp)
ns.configure({
    'django': {
        'port': 8000,
    },
})
