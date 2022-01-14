#!/bin/bash

pip uninstall ceres-nav
pip list --format=freeze > ../requirements.txt
cd ../
pip install -e .