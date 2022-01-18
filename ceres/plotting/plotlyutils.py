import plotly.graph_objects as go
import numpy as np
from typing import Union

default_axis = dict()

def plotly_random_color():
    return 'rgb({},{},{})'.format(np.random.randint(0,256),np.random.randint(0,256),np.random.randint(0,256))

def plotly_axisequal(fig):
    # Create the plots:
    max_range = -np.Inf
    min_range = np.Inf

    for plt in fig.data:
        min = np.min([plt.x.min(), plt.y.min(), plt.z.min()])
        if min < min_range:
            min_range = min
        max = np.max([plt.x.max(), plt.y.max(), plt.z.max()])
        if  max > max_range:
            max_range = max

    fig.layout.scene['xaxis']['range'] = [min_range,max_range]
    fig.layout.scene['yaxis']['range'] = [min_range,max_range]
    fig.layout.scene['zaxis']['range'] = [min_range,max_range]
    return fig

def plotly_orbit(orbit: np.ndarray, name=None, fig=None, line_color = 'black', line_width: int =2):
    """
    """

    # If now figure is provided, create a new one:
    if fig is None:
        fig = go.Figure()        

    trace = go.Scatter3d(x=orbit[0,:], y=orbit[1,:], z=orbit[2,:],name=name,
                         marker=dict(size=0.1), line=dict(color=line_color, width=line_width))

    # Add trace to the figure:
    fig.add_trace(trace)

    return fig