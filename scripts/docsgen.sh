#!/bin/bash
cd ..

# Clear out the directory:
mv docs/index.rst docs/index.rst.keep
rm docs/*.rst
rm -rf docs/html
rm -rf docs/doctrees
mv docs/index.rst.keep docs/index.rst

# Force rebuild:
sphinx-apidoc --force -o docs/ ceres/

# Make the HTML output:
cd docs/
make html