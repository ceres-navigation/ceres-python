
from ceres.plotting import plotly_planets,plotly_orbit,plotly_axisequal,plotly_random_color
from ceres.spiceutils import furnsh_directory, SpiceOrbit, SpiceRotation
from datetime import datetime, timedelta
from ceres.constants import *
import pandas as pd

# Furnsh the kernel containining saturn's moons:
furnsh_directory('kernels')

# Get the current time:
start_date = datetime.now()

# Calculate saturn's rotation relative to the J2000 frame:
saturn_sprot = SpiceRotation('IAU_SATURN')
saturn_rotation = saturn_sprot.rotation(start_date)

# Create a figure with Saturn:
fig = plotly_planets('saturn',rotation=saturn_rotation)

# List out the moons we want to simulate:
moon_names = ['Titan','Dione','Tethys','Enceladus']
for moon_name in moon_names:
    # Create a SpiceOrbit object for the current moon:
    moon = SpiceOrbit(moon_name, obs='SATURN')

    # Calculate the timespan required to plot a full orbit:
    stop_date = start_date + timedelta(seconds=moon.period(start_date, primary_body='Saturn', mu=muSaturn))
    tspan = pd.date_range(start_date, stop_date, 100)

    # Calculate the orbital states and add trajectory to plot:
    orbital_states = moon.states(tspan)
    plotly_orbit(orbital_states,name=moon_name,fig=fig,line_color=plotly_random_color(),line_width=2)

# Show the figure:
plotly_axisequal(fig)
fig.show()