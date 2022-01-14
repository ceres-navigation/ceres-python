from ceres.rotations import RotationMatrix
import numpy as np
from typing import Optional, Union, Sequence, Tuple

class Quaternion(RotationMatrix):
    def __new__(cls, quaternion: Optional[Union[Sequence,np.ndarray]] = [0,0,0,1]):
        return super().__new__(cls)

    def __init__(self,quaternion: Optional[Union[Sequence,np.ndarray]] = [0,0,0,1]):
        """
        """
        if quaternion is None:
            self._quaternion = np.array([0,0,0,1])
        else:
            self._quaternion = np.asarray(quaternion)

    @property
    def quaternion(self):
        return self._quaternion