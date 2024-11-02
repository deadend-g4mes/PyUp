from setuptools import setup, find_packages

setup(
    name='pyup',
      version='0.1.1',
      description='a python library for working with the LifeUp api',
      author='leighton carpenter',
      author_email='leighton.h.carpenter@gmail.com',
      packages=find_packages(),
      requires=[open('./requirements.txt')],
      )