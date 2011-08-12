# -*- coding: utf-8 -*-
from setuptools import setup

version = "0.0.1"
readme = open("README.rst").read()

setup(name="chesstournament",
      version=version,
      description="Play chess with your friends",
      long_description=readme,
      author="Ângelo Otávio Nuffer Nunes",
      author_email="angelonuffer@gmail.com",
      packages=["chesstournament"],
      )
