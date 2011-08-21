# -*- coding: utf-8 -*-
from setuptools import setup
import os

version = "0.0.1"
readme = open("README.rst").read()

os.system("msgfmt chesstournament/interface/locales/en/LC_MESSAGES/menu.po -o chesstournament/interface/locales/en/LC_MESSAGES/menu.mo")
os.system("msgfmt chesstournament/interface/locales/pt_BR/LC_MESSAGES/menu.po -o chesstournament/interface/locales/pt_BR/LC_MESSAGES/menu.mo")
setup(name="chesstournament",
      version=version,
      description="Play chess with your friends",
      long_description=readme,
      author="Ângelo Otávio Nuffer Nunes",
      author_email="angelonuffer@gmail.com",
      packages=["chesstournament"],
      )
      

