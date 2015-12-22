import os
import sys
from distutils.util import strtobool


def envdir(ctx, command, env=None):
    """Helper to wrap command in envdir command with given env."""
    return 'envdir {envdir} {command}'.format(
        envdir=os.path.join(ctx.base_dir, 'envs', env),
        command=command
    )


def confirmation_prompt(question):
    """Helper to ask user for confirmation."""
    sys.stdout.write("{} (y/n)\n".format(question))
    while True:
        try:
            return strtobool(input().lower())
        except ValueError:
            sys.stdout.write('Please respond with \'y\' or \'n\'.\n')
