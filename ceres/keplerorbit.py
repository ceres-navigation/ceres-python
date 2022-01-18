"""

"""
from typing import Optional, Union, Sequence, Tuple
import numpy as np

# from ceres import Rotation

class KeplerOrbit():
    """This is
    """
    def __init__(self,mu: float, elements: Union[list, np.ndarray], epoch: Union[np.ndarray, float], degrees: bool = False):
        """This is class allows for 

        :param mu: The standard graviational parameter :math:`(\mu)` of the central body
        :param elements: Keplerian orbital elements
        :param epoch: Epoch (reference time)
        :param degrees: Boolean to indicate whether the angular `elements` should be treated as degrees or radians.  Defaults to `False`
        """
        if type(elements) is list:
            elements = np.asarray(elements)

        if elements.ndim == 1:
            elements = elements.reshape((6,1))

        if degrees:
            elements[2:,:] = np.rad2deg(elements[2:,:])

        self._mu = mu
        self._epoch = epoch
        self._elements = elements


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
        ta = KeplerOrbit.mean_to_true_anomaly(M,e)

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
        if self._elements.shape[1] == 1:
            n = float(np.sqrt(self._mu/(self._elements[0,:]**3)))
        else:
            n = np.sqrt(self._mu/(self._elements[0,:]**3))
        return n

    @property
    def period(self):
        if self._elements.shape[1] == 1:
            T = float(2*np.pi/self.mean_motion)
        else:
            T = 2*np.pi/self.mean_motion
        return T


    @staticmethod
    def mean_to_true_anomaly(mean_anomaly,e):
        E = KeplerOrbit.mean_to_eccentric_anomaly(mean_anomaly,e)
        return KeplerOrbit.eccentric_to_true_anomaly(E,e)

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


    @staticmethod
    def states_to_elements(mu,states,tsince_epoch: float = 0):
        if states.ndim == 1:
            states.reshape((6,1))
        
        R = states[:3]
        V = states[3:]
        H = np.cross(R,V)
        r = np.linalg.norm(R)
        v = np.linalg.norm(V)

        # Calculate semi-major axis:
        a = 1/(2/r-v**2/mu)
        evec = np.cross(V,H)/mu-R/r
        e = np.linalg.norm(evec)

        ie = evec/e
        ih = H/np.linalg.norm(H)
        ip = np.cross(ih,ie)

        i = np.arccos(ih[2])
        RAAN = np.arctan2(ih[0],-ih[1])
        peri = np.arctan2(ie[2],ip[2])

        # Calculate the mean anomaly:
        sigma = np.dot(R,V)/np.sqrt(mu)
        E = np.arctan2(sigma/np.sqrt(a),1-r/a)
        M = E-e*np.sin(E)

        # Calculate mean anomaly at epoch based on provided time since epoch:
        n = np.sqrt(mu/(a**3))
        M0 = M - n*tsince_epoch

        return np.array([a,e,i,peri,RAAN,M0]).reshape((6,1))