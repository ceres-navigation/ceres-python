"""
"""
from ceres.constants import muSun
from ceres.spiceutils import time_to_et
import spiceypy as spice
import numpy as np
from datetime import date
from typing import Union

class SpiceRotation:
    """
    """
    def __init__(self,frame,ref='J2000'):
        """
        """
        self._frame = frame
        self._ref = ref

    def rotation(self, input_time):
        et = time_to_et(input_time)
        return spice.pxform(self._ref,self._frame,et)