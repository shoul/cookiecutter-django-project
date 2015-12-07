from invoke import ctask as task
from invoke import Collection

from . import helpers


@task
def create(ctx, env=None):
    """Create a new PostgreSQL database."""
    command = ''.join((
        'createdb -U {username} -l en_US.utf-8 -E utf-8 -O {username}',
        ' -T template0 -e {database}'
    ))
    command = command.format(
        database=ctx.db.database,
        username=ctx.db.username
    )
    ctx.run(helpers.envdir(ctx, command, env or ctx.env))


@task(name='create-user')
def create_user(ctx, env=None):
    """Create a new PostgreSQL user."""
    ctx.run(helpers.envdir(ctx, 'createuser -d -e {username}'.format(
        username=ctx.db.username), env or ctx.env,
    ))


@task
def drop(ctx, env=None, force=False):
    """Drop database."""
    interactive = '' if force else '-i'
    command = 'dropdb {interactive} -e -U {username} {database}'.format(
        database=ctx.db.database,
        interactive=interactive,
        username=ctx.db.username
    )
    ctx.run(helpers.envdir(ctx, command, env or ctx.env), pty=False)


@task(name='drop-user')
def drop_user(ctx, env=None, force=False):
    """Drop database user."""
    interactive = '' if force else '-i'
    command = 'dropuser {interactive} -e {username}'.format(
        interactive=interactive,
        username=ctx.db.username
    )
    ctx.run(helpers.envdir(ctx, command, env or ctx.env), pty=False)


ns = Collection(create, create_user, drop, drop_user)
ns.configure({
    'db': {
        'database': '{{ cookiecutter.repo_name }}',
        'username': '{{ cookiecutter.repo_name }}',
        'password': '{{ cookiecutter.repo_name }}',
    },
})
