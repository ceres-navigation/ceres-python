from ceres.keplerorbits import elements_to_state
from ceres.constants import muSun,AU,SPD
import numpy as np

def test_twobody():
    # Orbital elements for CERES (from SBDB):
    a = 2.766043062222408*AU
    e = 0.07850100198908602
    i = 10.58769305845201
    peri = 73.63703979153577
    RAAN = 80.26859547732911
    M = 291.3755993017663
    epoch = 2459600.5*SPD

    # Create the orbit instance:
    elements = np.array([a,e,i,peri,RAAN,M])
    states = elements_to_state(muSun,elements,0)
    

test_twobody()