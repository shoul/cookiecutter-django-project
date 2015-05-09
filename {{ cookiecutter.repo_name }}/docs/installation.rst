************
Installation
************

Development Setup
=================

Install the task execution tool `invoke <http://www.pyinvoke.org/>`_:

::

    $ pip install invoke

Install the packages for development:

::

    $ invoke develop

Then create the new PostgreSQL user and database:

::

    $ invoke db.create

The next step is to create the Django app(s) you want for the project:

::

    $ invoke django.startapp <appname>

Now create the database tables:

::

    $ invoke django.manage migrate

And start the development webserver:

::

    $ invoke django.runserver

To list the other :command:`invoke` tasks available simply run:

::

    $ invoke -l

.. note::

    You can save some keystrokes by using :command:`inv` instead of
    :command:`invoke`.
