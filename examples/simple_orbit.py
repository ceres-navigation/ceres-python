import numpy as np

from ceres.constants import muSun, AU, SPD
from ceres.orbits import TwoBody

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

# Desired epoch:
t = 2459499.500000000*SPD
r_truth = np.array([2.377195163333079E+08, 3.403674324622315E+08, -3.304222059618232E+07])
v_truth = np.array([-1.499949963514263E+01, 9.070482555326418E+00, 3.050109354260248E+00])

state = orbit.states(t)
print(state)

