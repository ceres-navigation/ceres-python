Installation
=============

To install `ceres` from `PyPI <https://pypi.org/project/ceres-nav/>`_:

.. code-block:: bash

   $ pip install ceres-env

Install from Source
*******************

To install `ceres` from `source <https://github.com/ceres-navigation/ceres>`_, first clone the respository:

.. code-block:: bash

   $ git clone git@github.com:ceres-navigation/ceres.git

Next, `cd` into the `ceres` root directory, and run:

.. code-block:: bash

    $ python -m pip install --upgrade pip
    $ pip install -r requirements.txt
    $ pip install -e .

To run tests:

..code-block:: bash

    $ pytest --cov-config=tests/.coveragerc --cov=ceres tests/