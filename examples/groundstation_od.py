"""
"""
import numpy as np
from datetime import datetime, timedelta

from ceres import CelestialBody, Spacecraft, TruthScene, EventsPlan
from ceres.constants import G, muEarth
from ceres.environment.gravity import PointMass
from ceres.plotting import plotly_orbit, plotly_planets, plotly_axisequal
from ceres.spiceutils import furnsh_directory, SpiceRotation
from ceres.keplerorbits import elements_to_state
from ceres.dynamics import rk4
from ceres.sensors import Radio, Antenna


# Define the equations of motion:
def simple(dt, X, *argv):
    r = X[:3]
    v = X[3:]

    # Unpack the models needed:
    earth = argv[0]

    # Get the acceleration:
    a = earth.gravity.get_acceleration(r)

    # Return the differential state:
    return np.vstack((v,a))


# Define the propagation model:
def dynamics(t_step, dt, objects):
    earth = objects[0]
    sat = objects[1]

    # Create the state vector:
    X = sat.state()

    # Run the RK4 algorithm:
    X = rk4(simple,dt,X, earth)

    sat.set_state(X)
    return 


# Define some ground stations:
frequency = 20E9 # 20GHz (K-Band)
ground_station1 = Radio(frequency, Antenna(position=[0,0,0]))
ground_station2 = Radio(frequency, Antenna(position=[0,0,0]))
ground_station3 = Radio(frequency, Antenna(position=[0,0,0]))

sat_radio = Radio(frequency, Antenna())

# Define the Earth:
earth_gravity = PointMass(muEarth)
earth = CelestialBody(gravity=earth_gravity,
                      sensors=[ground_station1, ground_station2, ground_station3])

# Define the satellite:
X0 = elements_to_state(muEarth,[7000,0,52.1,0,0,0],0)
satellite = Spacecraft(state=X0, rotation=np.eye(3), sensors=[sat_radio])

# Create the events plan:
start = datetime(2021,1,1,1)
end   = datetime(2021,1,1,2)
events_plan = EventsPlan(start,end)

# Add ground station 1 measurement times:
gs_times = np.arange(start, end, timedelta(seconds=30)).astype(datetime)
events_plan.add_measurement_plan(gs_times,ground_station1,'range',sat_radio)
events_plan.add_measurement_plan(gs_times,ground_station1,'doppler',sat_radio)
events_plan.add_measurement_plan(gs_times,ground_station2,'range',sat_radio)
events_plan.add_measurement_plan(gs_times,ground_station2,'doppler',sat_radio)
events_plan.add_measurement_plan(gs_times,ground_station3,'range',sat_radio)
events_plan.add_measurement_plan(gs_times,ground_station3,'doppler',sat_radio)

# Create the scene object:
scene = TruthScene(dynamics, [earth,satellite], events_plan)
scene.simulate()

# # Plot the results:
# fig = plotly_planets('earth',rotation=earth._rotation_log[:,:,-1], subsample=3)
# plotly_orbit(satellite._state_log,fig=fig, line_width=5, line_color='red')
# plotly_axisequal(fig)
# fig.show()

# Plot the measurements:
