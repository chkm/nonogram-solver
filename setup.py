from setuptools import setup, find_packages
from codecs import open
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nonogram-solver',
    version='0.1',
    description='A nonogram puzzle solver.',
    long_description=long_description,
    url='https://github.com/mprat/nonogram-solver',
    author='Michele Pratusevich',
    author_email='mprat@alum.mit.edu',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Indended Audience :: Other Audience',
        'Topic :: Games/Entertainment :: Puzzle Games',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='puzzles nonogram solver puzzle',

    packages=find_packages(exlcude=['tests', 'docs']),
    install_requires=['numpy'],
    extras_require={
        'test': ['pytest', 'pytest-cov', 'coverage']
    }
)
