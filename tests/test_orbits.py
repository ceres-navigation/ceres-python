from ceres.orbits import TwoBody
from ceres.constants import muSun,AU,SPD
import numpy as np

def test_twobody():
    # Orbital elements for CERES (from SBDB):
    a = 2.766043062222408*AU
    e = 0.07850100198908602
    i = np.deg2rad(10.58769305845201)
    peri = np.deg2rad(73.63703979153577)
    RAAN = np.deg2rad(80.26859547732911)
    M = np.deg2rad(291.3755993017663)
    epoch = 2459600.5*SPD

    # Create the orbit instance:
    orbit = TwoBody(muSun,'elements',np.array([a,e,i,peri,RAAN,M]),epoch)

test_twobody()