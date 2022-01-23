"""
"""
from abc import ABC

import numpy as np

class Component(ABC):
    """
    """
    def __init__(self, position = np.zeros(3), rotation: np.ndarray = np.eye(3)):
        """
        """
        position = np.asarray(position)
        if position.ndim == 1:
            position.reshape((3,1))

        self._position = position
        self._rotation = rotation

    def set_parent(self, parent):
        """
        """
        self._parent = parent

    def set_pose(self, position, rotation: np.ndarray):
        """
        """
        self._position = position
        self._rotation = rotation

    def set_position(self, position):
        """
        """
        self._position = position

    def set_rotation(self, rotation: np.ndarray):
        """
        """
        self._rotation = rotation

    def get_pose(self):
        """
        """
        parent_position, parent_rotation = self._parent.get_pose()
        return positiion, rotation

    def get_position(self):
        """
        """
        parent_position, parent_rotation = self._parent.get_pose()
        return position

    def get_rotation(self):
        """
        """
        parent_rotation = self._parent.get_rotation()
        return rotation