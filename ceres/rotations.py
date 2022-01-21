"""
"""

import numpy as np
from typing import Optional, Union, Tuple

def RotationMatrix0(t, degrees = False):
    if degrees:
        t = np.deg2rad(t)
    matrix = np.array([[1,       0,        0    ],
                       [0,  np.cos(t), np.sin(t)],
                       [0, -np.sin(t), np.cos(t)]])
    return matrix

def RotationMatrix1(t, degrees = False):
    if degrees:
        t = np.deg2rad(t)
    matrix = np.array([[np.cos(t), 0, -np.sin(t)],
                       [     0,    1,      0    ],
                       [np.sin(t), 0,  np.cos(t)]])
    return matrix
    
def RotationMatrix2(t, degrees = False):
    if degrees:
        t = np.deg2rad(t)
    matrix = np.array([[ np.cos(t), np.sin(t), 0],
                       [-np.sin(t), np.cos(t), 0],
                       [      0,        0,     1]])
    return matrix

def eulerangles_to_matrix(sequence: str, angles: np.ndarray, degrees: bool = False):
    """
    """
    assert type(sequence) is str, 'TODO'
    assert len(sequence) == 3, 'TODO'
    assert type(angles) is np.ndarray, 'TODO'
    assert angles.size == 3, 'TODO'
    if degrees:
        angles = np.deg2rad(angles)

    rotations = [RotationMatrix0,
                 RotationMatrix1,
                 RotationMatrix2]

    R0 = rotations[int(sequence[0])-1]
    R1 = rotations[int(sequence[1])-1]
    R2 = rotations[int(sequence[2])-1]

    return R2(angles[2])@R1(angles[1])@R0(angles[0])