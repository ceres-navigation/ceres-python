"""
"""
from re import sub
from matplotlib.pyplot import plot
import numpy as np
from datetime import datetime

from ceres.constants import muEarth
from ceres.plotting import plotly_orbit, plotly_planets

from ceres import RigidBody, CelestialBody, Spacecraft, Scene
from ceres.gravity import PointMass
from ceres.spiceutils import furnsh_directory, SpiceRotation
from ceres.keplerorbit import elements_to_state


# Define the equations of motion:
def simple(dt, X, earth):
    """
    """
    # Recover the states:
    r = X[:3]
    v = X[3:]

    # Update the position of the earth:
    earth.rotation(dt=dt)

    # Get the acceleration:
    a = earth.gravity.get_acceleration(r)

    # Return the differential state:
    return np.vstack((v,a))


# Define the propagation model:
def dynamics(t_step, dt, objects):
    earth = objects[0]
    sat = objects[1]

    # Update earth based on the current time:
    earth.update_et(t_step)

    # Create the state vector:
    X = sat.state()

    # Run the RK4 algorithm:
    k1 = dt*simple(0, X, earth)
    k2 = dt*simple(0.5*dt, X + 0.5*k1, earth)
    k3 = dt*simple(0.5*dt, X + 0.5*k2, earth)
    k4 = dt*simple(dt, X + k3, earth)
    X = X + (1/6)*(k1 + 2*k2 + 2*k3 + k4)

    sat.set_state(X)
    return 

# Furnsh some spice kernels:
furnsh_directory('kernels')

# Define the Earth:
earth_gravity = PointMass(muEarth)
earth_rotation = SpiceRotation('IAU_EARTH')
earth = CelestialBody(rotation=earth_rotation, gravity=earth_gravity)

# Define the satellite:
X0 = elements_to_state(muEarth,[7000,0,52.1,0,0,0],0)
satellite = Spacecraft(state=X0,rotation=np.eye(3))

# Create the scene object:
start = datetime(2021,1,1,12)
end = datetime(2021,1,1,14)
scene = Scene(dynamics, [earth,satellite], [start,end])
scene.simulate()

# Plot the results:
fig = plotly_planets('earth',subsample=3)
plotly_orbit(satellite._state_log, fig=fig, line_color='red', line_width=5)

fig.show()