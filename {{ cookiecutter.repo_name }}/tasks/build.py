from invoke import ctask as task


@task
def clean(ctx):
    """Remove build artifacts."""
    ctx.run('rm -fr build/')
    ctx.run('rm -fr dist/')
    ctx.run('rm -fr *.egg-info')


@task
def dist(ctx):
    """Create source distribution and show content."""
    ctx.run('python setup.py sdist bdist_wheel')
    ctx.run('ls -l dist')
