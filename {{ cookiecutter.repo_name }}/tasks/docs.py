import os
import webbrowser

from invoke import ctask as task
from invoke import Collection


@task(help={'builddir': "Sphinx build directory"})
def clean(ctx, builddir=None):
    """Remove documentation artifacts."""
    command = 'make -C {path} clean BUILDDIR={builddir}'.format(
        builddir=builddir or ctx.sphinx.build_dir,
        path=os.path.join(ctx.base_dir, 'docs')
    )
    ctx.run(command)


@task(help={'builddir': "Sphinx build directory", 'sphinxopts': "Sphinx options"})
def html(ctx, builddir=None, sphinxopts=None):
    """Build the project documentation as HTML."""
    command = 'make -C {path} html BUILDDIR={builddir} SPHINXOPTS=\'{sphinxopts}\''.format(
        builddir=builddir or ctx.sphinx.build_dir,
        path=os.path.join(ctx.base_dir, 'docs'),
        sphinxopts=sphinxopts or ''
    )
    ctx.run(command)


@task(help={'builddir': "Sphinx build directory"}, name='open')
def open_docs(ctx, builddir=None):
    """Open the project documentation in the default browser."""
    uri = 'file://{path}/docs/{builddir}/html/index.html'.format(
        path=os.getcwd(),
        builddir=builddir or ctx.sphinx.build_dir
    )
    webbrowser.open(uri)


@task(help={'builddir': "Sphinx build directory", 'port': "Port to use"})
def serve(ctx, builddir=None, port=None):
    """Serve the project documentation in the default browser."""
    webbrowser.open('http://127.0.0.1:{0}'.format(port or ctx.sphinx.port))
    command = 'cd docs/{builddir}/html; python -m SimpleHTTPServer {port}'.format(
        builddir=builddir or ctx.sphinx.build_dir,
        port=port or ctx.sphinx.port
    )
    ctx.run(command)


ns = Collection(clean, html, open_docs, serve)
ns.configure({
    'sphinx': {
        'build_dir': '_build',
        'port': 8080,
    },
})
