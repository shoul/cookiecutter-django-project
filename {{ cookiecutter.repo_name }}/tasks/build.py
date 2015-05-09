from invoke import ctask as task


@task
def clean(ctx):
    """Remove build artifacts"""
    ctx.run('rm -fr build/')
    ctx.run('rm -fr dist/')
    ctx.run('rm -fr *.egg-info')
