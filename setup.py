# -*- coding: utf-8 -*-
from setuptools import setup, find_packages, Extension
from setuptools.command.install import install
import subprocess
import os
from os.path import abspath, dirname, join

this_dir = abspath(dirname(__file__))
with open(join(this_dir, "LICENSE")) as f:
    license = f.read()

with open(join(this_dir, "README.md"), encoding="utf-8") as file:
    long_description = file.read()

with open(join(this_dir, "requirements.txt")) as f:
    requirements = f.read().split("\n")


setup(
    name="birds",
    version="0.1.0",
    description="Bayesian inference for differentiable simulators",
    url="https://github.com/arnauqb/birds",
    long_description_content_type="text/markdown",
    long_description=long_description,
    author="Ayush Chopra and Joel Dyer and Arnau Quera-Bofarull",
    author_email="arnauq@protonmail.com",
    license="MIT License",
    install_requires=requirements,
    packages=find_packages(exclude=["docs"]),
    include_package_data=True,
)
