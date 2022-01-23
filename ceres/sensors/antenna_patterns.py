"""
"""
from abc import ABC, abstractmethod
import numpy as np

class AntennaPattern(ABC):
    """
    """
    @abstractmethod
    def get_gain(self, direction: np.ndarray):
        pass


class Isotropic(AntennaPattern):
    """
    """
    def __init__(self):
        """
        """
    
    def get_gain(self, direction: np.ndarray):
        return 1


class Hemisphere(AntennaPattern):
    """
    """
    def __init__(self):
        """
        """
    def get_gain(self, direction: np.ndarray):
        """
        """
        if direction[2] >= 0:
            return 1
        else:
            return 0


class Cone(AntennaPattern):
    """
    """
    def __init__(self,half_angle):
        """
        """
        self._half_angle = half_angle
    
    def get_gain(self, direction: np.ndarray):
        """
        """
        angle = np.arccos(np.dot([0,0,1], direction/np.linalg.norm(direction)))
        if angle < self._half_angle:
            return 1
        else:
            return 0