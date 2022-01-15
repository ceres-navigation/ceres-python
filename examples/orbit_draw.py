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
t = np.arange(epoch, epoch + orbit.period, int(10*SPD))*SPD
states = orbit.states(t)

# import plotly.graph_objects as go

# Draw the orbit:
# fig = go.Figure(data=go.Scatter3d(
#     x=states[0,:], y=states[1,:], z=states[2,:],
# ))

# fig.show()
