from ceres.rotations import eulerangles_to_matrix
import numpy as np

def test_rotation():
    seq = '321'
    angles = np.array([1,1,1])
    matrix = eulerangles_to_matrix(seq, angles)
    assert type(matrix) is np.ndarray
    assert matrix.shape == (3,3)

test_rotation()