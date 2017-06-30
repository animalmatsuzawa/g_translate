#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='g_translate',
    version='0.1.0',
    description='Translate using google translation',
    long_description=readme,
    author='Toru Matsuzawa',
    author_email='animalmatsuzawa@gmail.com',
    url='https://github.com/animalmatsuzawa/g_translate',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['requests'],
    test_suite='tests'
)

