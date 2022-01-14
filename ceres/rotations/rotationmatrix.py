import numpy as np
from typing import Optional, Union, Sequence, Tuple

class RotationMatrix:
    def __new__(cls, matrix: Optional[np.ndarray] = np.eye(3)):
        return super().__new__(cls)

    def __init__(self,matrix: Optional[np.ndarray] = np.eye(3)):
        """
        """
        if matrix is None:
            self._matrix = np.eye(3)
        else:
            self._matrix = matrix

    @property
    def matrix(self):
        return self._matrix
