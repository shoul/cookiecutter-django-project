from invoke import ctask as task


@task
def clean(ctx):
    """Remove test and coverage artifacts"""
    ctx.run('rm -fr .cache/')
    ctx.run('rm -fr .tox/')
    ctx.run('coverage erase')
    ctx.run('rm -fr htmlcov/')
