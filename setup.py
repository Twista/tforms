from setuptools import setup, find_packages
import sys
from os import path

sys.path.insert(0, path.join(path.abspath(path.dirname(__file__)), "tforms"))
import tforms

setup(name='tforms',
      version=tforms.__version__,
      description="Python Form Library",
      classifiers=[
      ],
      keywords='',
      author='Michal Hatak',
      author_email='me@twista.cz',
      url='http://github.com/twista/tforms',
      license='MIT',
      packages=find_packages(exclude=[
          'venv', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
      ],
)
