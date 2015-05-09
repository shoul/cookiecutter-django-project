from invoke import ctask as task
from invoke import Collection


@task
def create(ctx):
    """Create a new PostgreSQL user and database"""
    print("You should use '{0}' as password for the new user.".format(ctx.db.password))
    ctx.run('createuser -d -e -P {0}'.format(ctx.db.username))
    ctx.run('createdb -U {username} {database}'.format(
        database=ctx.db.database,
        username=ctx.db.username
    ))


ns = Collection(create)
ns.configure({
    'db': {
        'database': '{{ cookiecutter.repo_name }}',
        'username': '{{ cookiecutter.repo_name }}',
        'password': '{{ cookiecutter.repo_name }}',
    },
})
