# -*- coding: utf-8 -*-
from setuptools import setup
import subprocess

version = "0.0.1"
readme = open("README.rst").read()

subprocess.call("./compile_locales.sh")

setup(name="chesstournament",
      version=version,
      description="Play chess with your friends",
      long_description=readme,
      author="Ângelo Otávio Nuffer Nunes",
      author_email="angelonuffer@gmail.com",
      license="MIT License",
      packages=["chesstournament"],
      )
