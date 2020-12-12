import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="persian",
    version="0.5.0",
    author="Reza Kamalifard",
    author_email="mrkamalifard@gmail.com",
    description="Simple Python library for Persian language localization",
    license="Apache License 2.0",
    keywords="example documentation tutorial",
    url="https://github.com/rezakamalifard/Persian",
    packages=['persian'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
)
