"""
"""
from ceres.constants import muSun
from ceres.keplerorbit import period, states_to_elements
from ceres.spiceutils import time_to_et
import spiceypy as spice
import numpy as np
from datetime import date
from typing import Union

class SpiceOrbit:
    """
    """
    def __init__(self,targ,ref='J2000',abcorr='NONE',obs='SOLAR SYSTEM BARYCENTER'):
        """
        """
        self._targ = targ
        self._ref = ref
        self._abcorr = abcorr
        self._obs = obs

    def states(self,input_time, ref=None,abcorr=None,obs=None):
        if ref is None:
            ref = self._ref
        if abcorr is None:
            abcorr = self._abcorr
        if obs is None:
            obs = self._obs

        et = time_to_et(input_time)

        orbital_states,_ = spice.spkezr(self._targ,et,ref,abcorr,obs)
        orbital_states = np.asarray(orbital_states).T
        return orbital_states
    
    def period(self,reference_time: Union[str,float,date], primary_body: str='SUN', mu: float =muSun):
        et = time_to_et(reference_time)
        orbital_states,_ = spice.spkezr(self._targ,et,'J2000','NONE',primary_body)
        elements = states_to_elements(mu,orbital_states,0)
        return period(mu,elements[0])
