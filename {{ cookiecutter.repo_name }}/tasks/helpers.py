import os


def envdir(ctx, command, env=None):
    """Helper to wrap command in envdir command with given env."""
    return 'envdir {envdir} {command}'.format(
        envdir=os.path.join(ctx.base_dir, 'envs', env),
        command=command
    )
