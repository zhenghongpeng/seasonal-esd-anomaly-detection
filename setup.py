import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "seasonal_esd",
    version = "0.0.1",
    author = "kp",
    author_email = "zhenghongpeng@yahoo.com",
    description = ("An demonstration of how to create, document, and publish "
                                   "to the cheese shop a5 pypi.org."),
    license = "ESD",
    keywords = "example documentation tutorial",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
        'numpy>=1.13.3',
        'pandas>=0.20.3',
        'scipy>=0.19.1',
        'statsmodels>=0.8.0',
    ],
)