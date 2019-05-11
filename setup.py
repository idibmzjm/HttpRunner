#encoding: utf-8
import io
import os
import sys
from shutil import rmtree

from setuptools import Command, find_packages, setup

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'apiautotest', '__about__.py'), encoding='utf-8') as f:
    exec(f.read(), about)

install_requires = [
    "requests",
    "PyYAML",
    "Jinja2",
    "har2case",
    "colorama",
    "colorlog",
    "requests_toolbelt",
    "filetype"
]


setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=about['__description__'],
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license="GPL",
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    packages=find_packages(exclude=["examples", "tests", "tests.*"]),
    package_data={
        '': ["README.md"],
        'apiautotest': ["templates/*"],
    },
    keywords='HTTP api test requests locust',
    install_requires=install_requires,
    extras_require={},
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    entry_points={
        'console_scripts': [
            'ate=apiautotest.cli:main_hrun',
            'apiautotest=apiautotest.cli:main_hrun',
            'hrun=apiautotest.cli:main_hrun',
            'locusts=apiautotest.cli:main_locust'
        ]
    }
)
