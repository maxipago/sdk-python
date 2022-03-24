# coding: utf-8
import re
import os
from setuptools import setup


def read_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    meta_filedata = read_file('maxipago/__init__.py')
    re_version = re.compile(r'VERSION\s*=\s*\((.*?)\)')
    group = re_version.search(meta_filedata).group(1)
    version = filter(None, map(lambda s: s.strip(), group.split(',')))
    return '.'.join(version)


setup(
    name='maxipago',
    version=get_version(),
    author='Stored',
    author_email='contato@stored.com.br',
    description='',
    license='MIT',
    keywords='',
    url='',
    packages=['maxipago',
              'maxipago.managers',
              'maxipago.managers.payment',
              'maxipago.requesters',
              'maxipago.requesters.payment',
              'maxipago.resources',
              'maxipago.utils'],
    long_description=read_file('README.md'),
    classifiers=[
        "Topic :: Utilities",
    ],
    install_requires=[
    ],
)
