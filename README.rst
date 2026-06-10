Introduction
============
.. image:: https://readthedocs.org/projects/cap-api/badge/?version=latest
    :target: https://cap-api.readthedocs.org/en/latest/
    :alt: Documentation Status

.. image:: https://github.com/relic-se/cap-api/workflows/Build%20CI/badge.svg
    :target: https://github.com/relic-se/cap-api/actions
    :alt: Build Status

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Code Style: Ruff

Python API integration library for Cap CAPTCHA server

Installing from PyPI
=====================
To install for current user:

.. code-block:: shell

    pip3 install cap-api

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install cap-api

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install cap-api

Usage Example
=============

.. code-block:: python

    from cap_api import Server
    server = Server("[serverDomain]", "[apiKey]")
    print(server.about)

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://cap-api.readthedocs.org/en/latest/>`_.

Contributing
============
Contributions are welcome!
