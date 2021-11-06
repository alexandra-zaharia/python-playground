from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0",
    packages=find_packages(),
    entry_points = {'console_scripts': [
        'capitalize = mypackage.__main__:main',
    ]},
)
