import numpy as np
from typing import Union, Tuple

class Rotation:
    def __init__(self,input_type: str, parameters: Union[np.ndarray, Tuple[Union[str,np.ndarray], np.ndarray]]):
        """
        """
        assert type(input_type) is str, 'TODO'
        assert len(parameters) >= 1, 'TODO'
        
        if input_type.lower() == 'matrix':
            assert type(parameters) is np.ndarray, 'TODO'
            assert parameters.shape == (3,3), 'TODO'
            self._matrix = parameters

        elif input_type.lower() == 'quaternion':
            assert type(parameters) is np.ndarray, 'TODO'
            assert parameters.shape == (4,1) or parameters.shape == (4,), 'TODO'
            self._matrix = Rotation.quaternion_to_matrix(parameters)

        elif input_type.lower() == 'eulerangles':
            assert type(parameters) is tuple, 'TODO'
            assert len(parameters) == 2, 'TODO'
            sequence = parameters[0]
            angles   = parameters[1]
            assert type(sequence) is str and len(sequence) == 3, 'TODO'
            assert type(angles) is np.ndarray, 'TODO'
            assert angles.size == 3, 'TODO'
            self._matrix = Rotation.eulerangles_to_matrix(sequence, angles)

        elif input_type.lower() == 'axisangle':
            assert type(parameters) is tuple, 'TODO'
            assert len(parameters) == 2, 'TODO'
            axis   = parameters[0]
            angle = parameters[1]
            assert type(axis) is np.ndarray and type(angle) is float, 'TODO'
            assert axis.size == 3 and angle.size == 1, 'TODO'
            self._matrix = Rotation.axisangle_to_matrix(axis,angle)


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