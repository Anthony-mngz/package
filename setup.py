from setuptools import setup, find_packages

requirements = ["toml", "PyYAML", "pandas", "numpy", "sqlalchemy"]

setup(
    name='helpers',
    version='1.1',
    install_requires=requirements,
    packages=find_packages(),
    url='https://github.com/Anthony-mngz/package/helpers.git',
    license='',
    author='Anthony',
    author_email='',
    description=''
)
