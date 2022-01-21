"""

"""
from typing import Optional, Union, Sequence, Tuple
import numpy as np

       
def mean_motion(mu,a):
    return np.sqrt(mu/(a**3))

def period(mu,a):
    return 2*np.pi/np.sqrt(mu/(a**3))

def elements_to_state(mu: float, elements: Union[Sequence, np.ndarray], tsince_epoch: float,
                      degrees = False):
    elements = np.asarray(elements)
    if elements.ndim == 1:
        elements = elements.reshape((6,1))

    if degrees:
        elements[2:,:] = np.deg2rad(elements[2:,:])

    a = elements[0,:]
    e = elements[1,:]
    i = elements[2,:]
    peri = elements[3,:]
    RAAN = elements[4,:]
    M0 = elements[5,:]

    M = M0 + mean_motion(mu,a)*(tsince_epoch)
    ta = mean_to_true_anomaly(M,e)

    h = np.sqrt(mu*a*(1-e**2))
    radial = ((h**2)/mu)*(1/(1+(e*np.cos(ta))))

    # Calculate states in PQW Coordinates:
    R_pqw = np.zeros((3,ta.size))
    R_pqw[0,:] = radial*np.cos(ta)     
    R_pqw[1,:] = radial*np.sin(ta)
    R_pqw[2,:] = 0
    V_pqw = np.zeros((3,ta.size))
    V_pqw[0,:] = (mu/h)*-np.sin(ta)
    V_pqw[1,:] = (mu/h)*(e+np.cos(ta))
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
    return np.vstack((r,v))


def mean_to_true_anomaly(mean_anomaly,e):
    E = mean_to_eccentric_anomaly(mean_anomaly,e)
    return eccentric_to_true_anomaly(E,e)


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


def eccentric_to_true_anomaly(E,e):
    return np.arctan2(np.sqrt(1-e**2)*np.sin(E),np.cos(E) - e)


def states_to_elements(mu,states,tsince_epoch: float):
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