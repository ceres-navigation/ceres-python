#!/bin/bash

# Remove previous builds/dists:
rm -rf dist/
rm -rf build/

# Upgrade if needed:
pip install --upgrade setuptools wheel twine

# Rebuild the distribution:
python setup.py sdist bdist_wheel

# Install locally:
pip install -e .

# Run unittest:

# This uploads it to test PyPI:
#python -m twine upload --repository testpypi dist/* 

# This is what uploads to PyPI when fully tested:
# python -m twine upload dist/*