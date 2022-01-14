#!/bin/bash

pip install sphinx
pip install sphinx-rtd-theme

sphinx-apidoc -o docs/ ceres/

cd docs/
make html