from setuptools import setup
import re

with open('nass/__init__.py', 'r') as f:
    version = re.search(r'__version__\s*=\s*\'([\d.]+)\'', f.read()).group(1)

if not version:
        raise RuntimeError('Couldn\'t find version string')

with open('README.rst', 'r') as f:
    readme = f.read()

with open('HISTORY.rst', 'r') as f:
    history = f.read()

setup(
    name='nass',
    version=version,
    description='USDA National Agricultural Statistics Service API wrapper',
    long_description=readme + '\n\n' + history,
    author='Nick Frost',
    author_email='nickfrostatx@gmail.com',
    url='https://github.com/nickfrostatx/nass',
    packages=['nass'],
    install_requires=['requests'],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    extras_require={
        'testing': ['pytest>=2.0.0'],
    },
)
