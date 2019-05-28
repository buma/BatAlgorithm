from setuptools import setup
import os
import sys

if sys.version_info[0] < 3:
    with open('README.md') as f:
        long_description = f.read()
else:
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()

setup(name='BatAlgorithm',
      description='Bat algorithm implementation',
      long_description_content_type="text/markdown",	
      long_description=long_description,
      author='Iztok Fister Jr. and Marko Burjek',
      version='0.3.1',
      license='MIT',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development'
      ],
      include_package_data=True,	
      url='https://github.com/buma/BatAlgorithm',
      py_modules=['BatAlgorithm']
      ) 

