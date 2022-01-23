"""
"""
from abc import ABC
import numpy as np
from .ray import Ray

import meshio

class Surface(ABC):
    """
    """
    def __init__(self):
        """
        """
        pass

    def ray_intersect(self, ray: Ray) -> np.ndarray:
        """
        """

class ShapeModel(Surface):
    """
    """
    def __init__(self, path_to_model: str):
        """
        """
        mesh_data = meshio.read(path_to_model)
        self._vertices = mesh_data.points
        self._triangles =  mesh_data.get_cells_type('triangle')


class Sphere(Surface):
    """
    """
    def __init__(self):
        """
        """