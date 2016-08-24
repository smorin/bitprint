#!/usr/bin/env python

import os
import os.path
import sys
from glob import glob

# sys.path.insert(0, os.path.abspath('src'))

# import bitprint
try:
    from setuptools import setup
except ImportError:
    print ("bitprint now needs setuptools in order to build. ")
    print ("Install it using your package manager (usually python-setuptools) or via pip (pip install setuptools).")
    sys.exit(1)


from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    """
    This is the custom test command class to overwrite the default setuptools 
    test command behavior.
    
    This is instead running the module 'pytest' which will be auto installed
    by setup tools when you run 'python setup.py test'
    
    The following to commands are equivalent 
    
    python setup.py test -a "--durations=5"
    
    py.test --durations=5
    
    Reference: https://pytest.org/latest/goodpractices.html
    """
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        
        self.pytest_args = ['--ignore=bitprint-virtualenv', '--ignore=bitprint-venv', '--ignore=tasks', '--ignore=test_data'] + self.pytest_args
        
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


from setuptools import find_packages

version = ''

with open('VERSION') as file:
    version = file.readline()
    version = version.rstrip()

with open('README.rst') as file:
    long_description = file.read()



requires = ['Click']
test_requirements = ['pytest>=2.9.2', 'pytest-cov']

test_data_files = []

for dirpath, dirnames, files in os.walk('test_data'):
    # you can't add directories to data_files
    # test_data_files.append(dirpath) 
    for filename in files:
        test_data_files.append(os.path.join(dirpath,filename))

# this doesn't add it to the source distribution - you need to add it to the MANIFEST.in
test_data_files.append('VERSION')

setup(
    name='bitprint',
    author='Steve Morin',
    author_email='steve@stevemorin.com',
    version=version,
    url='https://github.com/smorin/bitprint',
    include_package_data=True,
    install_requires=requires,
    entry_points='''
        [console_scripts]
        bitprint=bitprint:cli
    ''',
    py_modules=['bitprint'],
    data_files=[('test_data', test_data_files)],
    # package_dir = {'':'.'},
    # packages=find_packages('.'),
    # packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "test"]),
    description='bitprint file utilities dedup, only file copy detection, empty dir detection',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: Other/Proprietary License',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Operating System :: POSIX :: BSD',        
    ],
    long_description=long_description,
	tests_require=test_requirements, 
	keywords=[
        'dedup', 'file cleanup', 'empy dirs', 'duplicate file detection',
    ],
    cmdclass={'test': PyTest},
)




