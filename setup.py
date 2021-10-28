from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.md')) as f:
    readme = f.read()

setup(
    name             = 'office_convert',
    version          = '0.0.2',
    description      = 'Excel and ODS Spreadsheet to CSV Converter',
    long_description = readme,
    author           = 'FNNDSC',
    author_email     = 'dev@babyMRI.org',
    url              = 'https://github.com/FNNDSC/pl-office-convert#readme',
    packages         = ['office_convert'],
    install_requires = ['chrisapp', 'tqdm', 'pandas', 'odfpy', 'openpyxl'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'office_convert = office_convert.__main__:main'
            ]
        }
)
