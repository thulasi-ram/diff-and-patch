import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='diff-and-patch',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='GNU GPLv3',
    description='A simple python package which serves as a framework for diffing and patching complex objects. '
                'Inspired by Shreyas Kulkarni and git diff and patch.',
    long_description=README,
    url='https://github.com/thulasi-ram/diff-and-patch',
    author='Damodharan Thulasiram',
    author_email='thulasi503@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
    ],
    python_requires='>2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    keywords='python diff patch differ patcher',
    py_modules=["six"],
    project_urls={
        'Documentation': 'https://github.com/thulasi-ram/diff-and-patch',
        'Source': 'https://github.com/thulasi-ram/diff-and-patch',
        'Tracker': 'https://github.com/thulasi-ram/diff-and-patch/issues',
    },
)
