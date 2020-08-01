#!/usr/bin/env python
import setuptools

setuptools.setup(
    name="cto",
    version="0.2.0",
    description="Comment-To-Object: a metadata translator for databases",
    author="Stephen Bailey",
    url="http://github.com/immuta/cto",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    packages=setuptools.find_packages(),
    py_modules=["cto"],
    include_package_data=True,
)
