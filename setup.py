# encoding: utf-8
import re
from codecs import open
from setuptools import setup, find_packages
from os import path

HERE = path.abspath(path.dirname(__file__))


def read(*names):
    with open(path.join(HERE, *names)) as stream:
        return stream.read()


def find_info(info, *file_paths):
    content = read(*file_paths)
    matching = re.search(
        r'''^__{}__ = ['"]([^'"]*)['"]'''.format(info),
        content,
        re.M
    )
    if matching:
        return matching.group(1)
    raise RuntimeError('Unable to find {} string.'.format(info))


LONG_DESCRIPTION = read('README.md')
VERSION = find_info('version', 'maxipago', '__init__.py')
AUTHOR = find_info('author', 'maxipago', '__init__.py')
AUTHOR_EMAIL = find_info('contact', 'maxipago', '__init__.py')
LICENSE = find_info('license', 'maxipago', '__init__.py')

setup(
    name='maxipago',
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description='',
    license=LICENSE,
    keywords='',
    url='https://github.com/loggi/Python-integration-lib/',
    packages=find_packages(),
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Topic :: Utilities",
    ],
    install_requires=(
        'requests==2.4.3',
        'lxml==3.4.0',
    ),
)
