from ceres.geometry import ShapeModel
from ceres.plotting import plotly_mesh, plotly_light

import numpy as np
import plotly.graph_objects as go

obj = ShapeModel('data/bennu.obj')

fig = plotly_mesh(obj, show_edges=False)

# plotly_light(fig)

fig.show()