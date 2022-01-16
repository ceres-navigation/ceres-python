from ceres.rotations import Rotation
import numpy as np

def test_rotation():
    r = Rotation()
    assert (r.matrix == np.eye(3)).all()

    assert (r.quaternion == np.array([0,0,0,1])).all()

test_rotation()