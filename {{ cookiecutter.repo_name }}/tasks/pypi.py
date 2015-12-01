import webbrowser

from invoke import ctask as task


@task(name="test-upload")
def test_upload(ctx):
    """Test upload a release to test PyPI using twine."""
    ctx.run('twine upload -r test -s dist/*')
    webbrowser.open('https://testpypi.python.org/pypi/{pkg_name}'.format(ctx.pkg_name))


@task
def upload(ctx):
    """Upload a release to PyPI using twine."""
    ctx.run('twine upload -s dist/*')
    webbrowser.open('https://pypi.python.org/pypi/{pkg_name}'.format(ctx.pkg_name))
