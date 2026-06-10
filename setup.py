# SPDX-FileCopyrightText: Copyright (c) 2026 Cooper Dalrymple (@relic-se)
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os

from setuptools import setup

PACKAGE = "cap_api"

info = {}
dirpath = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(dirpath, PACKAGE, "__version__.py"), encoding="utf-8") as f:
    exec(f.read(), info)

with open("README.rst", encoding="utf-8") as f:
    readme = f.read()

setup(
    name=info["__title__"],
    version=info["__version__"],
    description="Python wrapper for Cap CAPTCHA server API",
    long_description=readme,
    long_description_content_type="text/plain",
    url="https://github.com/relic-se/cap-api",
    author=info["__author__"],
    author_email="me@dcdalrymple.com",
    license=info["__license__"],
    packages=[PACKAGE],
    python_requires=">=3.7, <4",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
    ],
)
