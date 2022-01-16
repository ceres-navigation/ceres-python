import numpy as np
from typing import Optional, Union, Tuple

class Rotation:
    def __init__(self,input_type: Optional[str] = None, input_value: Optional[Union[np.ndarray, Tuple[Union[str,np.ndarray], np.ndarray]]] = None):
        """
        """
        if input_type is None:
            assert input_value is None, 'TODO'
        if input_value is None:
            assert input_type is None, 'TODO'

        if input_type is None:
            self._matrix = np.eye(3)
            return

        assert type(input_type) is str, 'TODO'
        assert len(input_value) >= 1, 'TODO'
        
        if input_type.lower() == 'matrix':
            assert type(input_value) is np.ndarray, 'TODO'
            assert input_value.shape == (3,3), 'TODO'
            self._matrix = input_value

        elif input_type.lower() == 'quaternion':
            assert type(input_value) is np.ndarray, 'TODO'
            assert input_value.shape == (4,1) or input_value.shape == (4,), 'TODO'
            self._matrix = Rotation.quaternion_to_matrix(input_value)

        elif input_type.lower() == 'eulerangles':
            assert type(input_value) is tuple, 'TODO'
            assert len(input_value) == 2, 'TODO'
            sequence = input_value[0]
            angles   = input_value[1]
            assert type(sequence) is str and len(sequence) == 3, 'TODO'
            assert type(angles) is np.ndarray, 'TODO'
            assert angles.size == 3, 'TODO'
            self._matrix = Rotation.eulerangles_to_matrix(sequence, angles)

        elif input_type.lower() == 'axisangle':
            assert type(input_value) is tuple, 'TODO'
            assert len(input_value) == 2, 'TODO'
            axis   = input_value[0]
            angle = input_value[1]
            assert type(axis) is np.ndarray and type(angle) is float, 'TODO'
            assert axis.size == 3 and angle.size == 1, 'TODO'
            self._matrix = Rotation.axisangle_to_matrix(axis,angle)

    @property
    def matrix(self):
        return self._matrix

    @property
    def quaternion(self):
        return None


    @staticmethod
    def eulerangles_to_matrix(sequence, angles):
        """
        """
        assert type(sequence) is str, 'TODO'
        assert len(sequence) == 3, 'TODO'
        assert type(angles) is np.ndarray, 'TODO'
        assert angles.size == 3, 'TODO'

        rotations = [Rotation.RotationMatrix0,
                     Rotation.RotationMatrix1,
                     Rotation.RotationMatrix2]

        R0 = rotations[int(sequence[0])-1]
        R1 = rotations[int(sequence[1])-1]
        R2 = rotations[int(sequence[2])-1]

        return R2(angles[2])*R1(angles[1])*R0(angles[0])
    
    @staticmethod
    def RotationMatrix0(t):
        matrix = np.array([[1, 0, 0],[0, np.cos(t), np.sin(t)],[0, -np.sin(t), np.cos(t)]])
        return matrix

    @staticmethod
    def RotationMatrix1(t):
        matrix = np.array([[np.cos(t), 0, -np.sin(t)],[0, 1, 0],[np.sin(t), 0, np.cos(t)]])
        return matrix

    @staticmethod
    def RotationMatrix2(t):
        matrix = np.array([[np.cos(t), np.sin(t), 0],[-np.sin(t), np.cos(t), 0],[0, 0, 1]])
        return matrix