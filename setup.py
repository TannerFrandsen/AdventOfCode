from setuptools import find_packages, setup

setup(
    name='AdventOfCode',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/TannerFrandsen/AdventOfCode',
    author='Tanner Frandsen',
    author_email='tandaman29@gmail.com',
    description='The Advent of code',
    long_description=__doc__,
    setup_requires=["flake8"],
    install_requires=["flake8"],
    tests_require=['pytest==5.4.1']
)
