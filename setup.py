from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="h3xrecon_cli",
    version="0.0.1",
    author="@h3xitsec",
    author_email="connect@h3x.it",
    description="CLI for h3xrecon bug bounty reconnaissance automation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/h3xitsec/h3xrecon-cli",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "docopt",
        "loguru",
        "tabulate",
        "nats-py",
        "asyncpg",
        "h3xrecon-core @ git+https://github.com/h3xitsec/h3xrecon-core.git@main"
    ],
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'h3xrecon=h3xrecon_cli.main:main',
        ],
    },
)