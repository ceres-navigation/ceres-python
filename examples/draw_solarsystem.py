from datetime import date, timedelta
import pandas as pd
import numpy as np

from ceres.spiceutils import SpiceOrbit, furnsh_directory
from ceres.plotting import plotly_orbit, plotly_axisequal

# Furnsh the appropriate SPICE kernels:
furnsh_directory('kernels')

# Get today's date:
start_date = date.today()

# Define the orbits for each planet:
ref = 'ECLIPJ2000'
obs = 'SUN'
planet_names = ["Mercury", "Venus", "Earth", "Mars Barycenter", "Jupiter Barycenter",
                "Saturn Barycenter", "Uranus Barycenter", "Neptune Barycenter"]

# Loop through all of the planets:
fig = None
for planet_name in planet_names:
    # Create a SPICE Orbit object:
    planet = SpiceOrbit(targ=planet_name,ref=ref,obs=obs)

    # Calculate the stop date after one complete orbit:
    stop_date = start_date + timedelta(seconds=planet.period(date.today()))

    # Create a date range to solve for orbital states from:
    tspan = pd.date_range(start_date, stop_date, 100)

    # Calculate the position of the current planet:
    orbital_states = planet.states(tspan)

    # Add the current planet to the figure:
    color = 'rgb({},{},{})'.format(np.random.randint(0,256),np.random.randint(0,256),np.random.randint(0,256))
    fig = plotly_orbit(orbital_states, fig=fig, line_color=color)

# Show the figure:
plotly_axisequal(fig)
fig.show()