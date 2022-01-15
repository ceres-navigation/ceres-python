# CERES
**C**elestial **E**stimation for **R**esearch, **E**xploration, and **S**imulation

![Tests](https://github.com/ceres-navigation/ceres/actions/workflows/tests.yml/badge.svg)
[![codecov](https://codecov.io/gh/ceres-navigation/ceres/branch/main/graph/badge.svg?token=BX07Q0PITB)](https://codecov.io/gh/ceres-navigation/ceres)
[![GitHub issues](https://img.shields.io/github/issues/ceres-navigation/ceres)](https://github.com/ceres-navigation/ceres/issues)
[![GitHub Release](https://img.shields.io/github/v/release/ceres-navigation/ceres)](https://github.com/ceres-navigation/ceres/releases)
[![PyPI version](https://badge.fury.io/py/ceres-nav.svg)](https://pypi.org/project/ceres-nav/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[CERES](https://ceresnavigation.org) provides an API for:
- Simulating spacecraft dynamics
- Developing new navigation and mapping algorithms
- Modeling sensors and other measurements
- Implementing kalman filters and other estimation schemes

Releases are [registed on PyPI](https://pypi.org/project/ceres-nav/), while development is occuring on the [ceres GitHub page](https://github.com/ceres-navigation/ceres).  Any bugs should be reported to the [Issue Tracker](https://github.com/ceres-navigation/ceres/issues).  Documentation is located at [docs.ceresnavigation.org](https://docs.ceresnavigation.org)


# Install
- **Install:** 
    - `pip install ceres-nav`
- **Import:** 
    - `import ceres`

*To install from source for development purposes, please see the [Develop](#develop) section.*

## Additional Steps for Windows Subsystem for Linux
### Windows 11 Insider (RECOMMENDED):
- [Install support for Linux GUI apps](https://docs.microsoft.com/en-us/windows/wsl/tutorials/gui-apps)

### Windows 10/11:
*NOTE: This is required in order to graphically display outputs from WSL2.*

- Downalod and install [VcXsrv](https://sourceforge.net/projects/vcxsrv/)
- Run `sudo apt-get install python-tk`
- Add `export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0` to the bottom of your `~/.bashrc` file
- In windows settings, go to `Firewall & network protection` -> `Allow an app through firewall` and make sure that VcXsrv has both public and private checked.
- Launch VcXsrv with "Disable access control" ticked.


## Develop
To contribute to this project, it is highly recommended that you create a virtual environment with either mamba or conda.
1. Install mamba or conda:
    - To install mamba (RECOMENDED): [mambaforge](https://github.com/conda-forge/miniforge#mambaforge)
    - To install conda: [anaconda](https://www.anaconda.com/products/individual)
2. Create the virtual environment:
    - source the base environment
    - create `ceres_env` environment with ceres dependencies: `conda create -n ceres_env python=3 --file requirements.txt`
    - Activate the virtual environment with `conda activate ceres_env`
3. Installing CERES into the environment:
   - Clone: `git clone https://github.com/ceres-navigation/ceres`
   - Install: `cd ceres; pip install -e .`
4. Running tests:
   - `pytest --cov-config=.coveragerc --cov=ceres tests/`

If you are new to contributing to open source, [this
guide](https://opensource.guide/how-to-contribute/) helps explain why, what,
and how to successfully get involved.

# Contact
All questionsm, comments, and concerns should be directed to Chris Gnam: crgnam@buffalo.edu

# Attributions
## Solar System Scope
[Solar System Scope](https://www.solarsystemscope.com) provides free textures of celestial bodies, licensed under the [Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  These textures are used in CERES for visualization purposes, and were obtained from: https://www.solarsystemscope.com/textures/.  No alterations were made to these textures, and all copyright belongs to Solar System Scope.