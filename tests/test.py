import pytest
import pkg_resources

def test():
    retcode = pytest.main(["--cov-config=ceres/tests/.coveragerc", "--cov=ceres ceres/tests/"])

if __name__ == "__main__":
    test()