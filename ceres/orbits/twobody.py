from sre_parse import State
from typing import Optional, Union, Sequence, Tuple
import numpy as np

from ceres import Rotation

class TwoBody():
    def __init__(self,mu: float, input_type: str, values: np.ndarray, epoch: np.ndarray):
        """
        """
        assert type(mu) is float, 'TODO'
        assert type(epoch) is np.ndarray or float, 'TODO'
        if type(epoch) is np.ndarray:
            assert epoch.size == values.size/6, 'TODO'

        self._mu = mu
        self._epoch = epoch

        # Verify the input is the correct size:
        assert type(input_type) is str, 'TODO'
        assert type(values) is np.ndarray, 'TODO'
        
        assert values.ndim == 1 or values.ndim == 2, 'TODO'
        assert values.shape[0] == 6, 'TODO'


        if values.ndim == 1:
            values = values.reshape((6,1))

        if input_type.lower() == 'elements':
            self._elements = values
            self.states(self._epoch)

        elif input_type.lower() == 'states':
            self._states = values
            self.elements(self._epoch)
        else:
            raise ValueError('input_type ')


    def states(self,time):
        """
        """
        a = self._elements[0,:]
        e = self._elements[1,:]
        i = self._elements[2,:]
        peri = self._elements[3,:]
        RAAN = self._elements[4,:]
        M0 = self._elements[5,:]

        M = M0 + self.mean_motion*(time - self._epoch)
        ta = TwoBody.mean_to_true_anomaly(M,e)

        h = np.sqrt(self._mu*a*(1-e**2))
        radial = ((h**2)/self._mu)*(1/(1+(e*np.cos(ta))))

        # Calculate states in PQW Coordinates:
        R_pqw = np.zeros((3,ta.size))
        R_pqw[0,:] = radial*np.cos(ta)     
        R_pqw[1,:] = radial*np.sin(ta)
        R_pqw[2,:] = 0
        V_pqw = np.zeros((3,ta.size))
        V_pqw[0,:] = (self._mu/h)*-np.sin(ta)
        V_pqw[1,:] = (self._mu/h)*(e+np.cos(ta))
        V_pqw[2,:] = 0

        # Define the transformation from PQW to Inertial:
        a1 = -np.sin(RAAN)*np.cos(i)*np.sin(peri) + np.cos(RAAN)*np.cos(peri)
        a2 = -np.sin(RAAN)*np.cos(i)*np.cos(peri) - np.cos(RAAN)*np.sin(peri)
        a4 =  np.cos(RAAN)*np.cos(i)*np.sin(peri) + np.sin(RAAN)*np.cos(peri)
        a5 =  np.cos(RAAN)*np.cos(i)*np.cos(peri) - np.sin(RAAN)*np.sin(peri)
        a7 =  np.sin(peri)*np.sin(i)
        a8 =  np.cos(peri)*np.sin(i)

        # Apply the transformation:
        r = np.stack((a1*R_pqw[0,:] + a2*R_pqw[1,:], a4*R_pqw[0,:] + a5*R_pqw[1,:], a7*R_pqw[0,:] + a8*R_pqw[1,:]), axis=0)
        v = np.stack((a1*V_pqw[0,:] + a2*V_pqw[1,:], a4*V_pqw[0,:] + a5*V_pqw[1,:], a7*V_pqw[0,:] + a8*V_pqw[1,:]), axis=0)
        self._states = np.vstack((r,v))
        return self._states

    @property
    def mean_motion(self):
        return np.sqrt(self._mu/(self._elements[0,:]**3))

    @property
    def period(self):
        return 2*np.pi/self.mean_motion


    @staticmethod
    def mean_to_true_anomaly(mean_anomaly,e):
        E = TwoBody.mean_to_eccentric_anomaly(mean_anomaly,e)
        return TwoBody.eccentric_to_true_anomaly(E,e)

    @staticmethod
    def mean_to_eccentric_anomaly(M,e,tol=1e-12,iters=100):
        # Solve for the eccentric anomaly:
        E = np.zeros(M.shape)
        for idx, m in enumerate(M):
            En = m
            for ii in range(0,iters):
                Ens = En = En - (En-e*np.sin(En) - m)/(1 - e*np.cos(En))
                if np.abs(Ens-En) < tol:
                    break
                En = Ens
            E[idx] = Ens
        return E

    @staticmethod
    def eccentric_to_true_anomaly(E,e):
        return np.arctan2(np.sqrt(1-e**2)*np.sin(E),np.cos(E) - e)