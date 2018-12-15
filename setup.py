#from distutils.core import setup
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()
setup(
    # Application name:
    name="YAMS",

    # Version number (initial):
    version="0.5",

    # Application author details:
    author="Derin Yarsuvat",
    author_email="derin@ml1.net",

    license='GPLv3',

    # Packages
    packages=['yams' ],

    package_data={
        },

    # Include additional files into the package
    include_package_data=False,

    # Details
    url="https://github.com/berulacks/yams",
    download_url="https://github.com/Berulacks/yams/releases/download/v0.5/yams-0.5-py3-none-any.whl",

    #
    # license="LICENSE.txt",
    description="Yet Another MPD Scrobbler (for Last.FM!)",

    long_description=readme(),
    long_description_content_type='text/markdown',

    scripts=[
        'bin/yams'
        ],

    # Dependent packages (distributions)
    install_requires=[
        'python-mpd2==1.0.0',
        'PyYAML==4.2b4'
    ],
    python_requires='>=3',
    zip_safe=False
)
