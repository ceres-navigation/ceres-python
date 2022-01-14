from ceres.rotations import RotationMatrix, Quaternion
import numpy as np

def test_rotation_matrix():
    r = RotationMatrix()
    assert (r.matrix == np.eye(3)).all()

    matrix = np.array([[1,1,1],[2,2,2],[3,3,3]])
    r = RotationMatrix(matrix)
    

def test_quaternion():
    q = Quaternion()
    assert (q.quaternion == np.array([0,0,0,1])).all()
    

test_rotation_matrix()
test_quaternion()