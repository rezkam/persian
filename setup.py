import os
from setuptools import setup

setup(
    name = "persian",
    version = "0.0.4",
    author = "Mohammad Reza Kamalifard, Keyvan Hedayati, Bahram Aghaei",
    author_email = "mr.kamalifard@gmail.com, k1.hedayati93@gmail.com, aghaee.bahram@gmail.com",
    description = ("A mature Python library for converting Arabic/English numbers and characters to Persian and vice versa"),
    license = "MIT",
    keywords = ["encoding","persian2eng", "eng2persian"],
    url = "http://packages.python.org/persian",
    packages=['persian'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
)
