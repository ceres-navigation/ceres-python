import numpy as np

class TwoBody():
    def __init__(self,mu,r=None,v=None,state=None,
                 a=None,e=None,i=None,w=None,RAAN=None,ma=None,ta=None):
        """
        """
        # Check if a state vector has be set:
        if state is not None:
            assert not any([r,v,a,e,i,w,RAAN,ma,ta]), "If state (state vector) is set, no position/veloecity or orbital elements can be set"

        # Check if position/velocity pair have been set:
        if r is not None:
            assert v is not None, "If r (position) is set, v (velocity) must also be set"
        if v is not None:
            assert r is not None, "If v (velocity) is set, r (position) must also be set"

        if None not in (r,v):
            assert not any([a,e,i,w,RAAN,ma,ta,state]), "If r and v (position/velocity) are set, no orbital elements or state vector can be set"

        # Check if orbital elements have been set:
        missing_elem_error = "If {} is set, elements: all other elements, and either ma (mean anommaly) or ta (true anomaly), must also be set"
        if a is not None:
            assert None not in (a,e,i,w,RAAN), missing_elem_error.format('a (semi-major axis)')
        if e is not None:
            assert None not in (a,e,i,w,RAAN), missing_elem_error.format('e (eccentricity)')
        if i is not None:
            assert None not in (a,e,i,w,RAAN), missing_elem_error.format('i (inclination)')
        if w is not None:
            assert None not in (a,e,i,w,RAAN), missing_elem_error.format('w (argument of periapsis')
        if RAAN is not None:
            assert None not in (a,e,i,w,RAAN), missing_elem_error.format('RAAN (Right Ascension of Ascending Node)')

        # 

        # Store the values:
        self._mu = mu
        self._a = a
        self._e = e
        self._i = i
        self._w = w
        self._RAAN = RAAN
        self._ma = ma
        self._ta = ta

        self._r = r
        self._v = v

    @property
    def mu(self):
        return self._mu

    @mu.setter
    def mu(self,mu):
        self._mu = mu
