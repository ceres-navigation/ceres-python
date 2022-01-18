import numpy as np

from ceres.constants import muSun, AU, SPD
from ceres import KeplerOrbit
from ceres.plotting import plotly_orbit

# Orbital elements for CERES (from SBDB):
epoch = 2459600.5*SPD
a = 2.766043062222408*AU
e = 0.07850100198908602
i = 10.58769305845201
peri = 73.63703979153577
RAAN = 80.26859547732911
M = 291.3755993017663

# Create the orbit instance:
elements = np.array([a,e,i,peri,RAAN,M])
orbit = KeplerOrbit(muSun,elements,epoch,degrees=True)

# Create a time history to calculate the position at:
start_time = epoch
end_time = epoch + orbit.period/SPD
dt = 10 # days
t = np.arange(start_time, end_time, dt)*SPD
states = orbit.states(t)

# Plot the orbit:
fig = plotly_orbit(states,line_color='rgb(255, 0, 0)')
fig.show()