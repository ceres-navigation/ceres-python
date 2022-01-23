import plotly.graph_objects as go
import numpy as np
from typing import Union

from PIL import Image, ImageOps
import pkg_resources
from ceres.constants import *

grey_colormap =[[0.0, 'rgb(0, 0, 0)'],[1.0, 'rgb(255, 255, 255)']]
sun_colormap = [[0.0, 'rgb(191, 30, 3)'],
                [0.2, 'rgb(217, 81, 12)'],
                [0.4, 'rgb(245, 101, 17)'],
                [0.6, 'rgb(254, 178, 46)'],
                [1.0, 'rgb(255, 254, 222)']]
venus_colormap = [[0.0, 'rgb(160, 125, 60)'],
                  [0.4, 'rgb(170, 135, 82)'],
                  [0.6, 'rgb(195, 157, 98)'],
                  [0.8, 'rgb(243, 204, 141)'],
                  [1.0, 'rgb(253, 219, 165)']]
earth_colormap = [[0.0, 'rgb(30, 59, 117)'],
                    [0.1, 'rgb(46, 68, 21)'],
                    [0.2, 'rgb(74, 96, 28)'],
                    [0.3, 'rgb(115,141,90)'],
                    [0.4, 'rgb(122, 126, 75)'],
                    [0.6, 'rgb(122, 126, 75)'],
                    [0.7, 'rgb(141,115,96)'],
                    [0.8, 'rgb(223, 197, 170)'],
                    [0.9, 'rgb(237,214,183)'],
                    [1.0, 'rgb(255, 255, 255)']]
mars_colormap = [[0.0, 'rgb(44, 35, 36)'],
                 [0.1, 'rgb(74, 49, 45)'],
                 [0.5, 'rgb(205, 94, 60)'],
                 [0.6, 'rgb(217, 96, 55)'],
                 [0.8, 'rgb(252, 145, 92)'],
                 [0.96, 'rgb(255,255,255)'],
                 [1.0, 'rgb(255,255,255)']]
jupiter_colormap = [[0.0, 'rgb(0, 0, 0)'],
                    [0.55, 'rgb(175, 130, 100)'],
                    [1.0, 'rgb(225, 220, 220)']]
saturn_colormap = [[0.0, 'rgb(139, 150, 146)'],
                   [0.3, 'rgb(157, 141, 126)'],
                   [0.4, 'rgb(180, 165, 135)'],
                   [0.5, 'rgb(183, 170, 138)'],
                   [0.6, 'rgb(189, 169, 134)'],
                   [0.7, 'rgb(209, 186, 143)'],
                   [0.9, 'rgb(237, 209, 169)'],
                   [1.0, 'rgb(255, 239, 214)']]
uranus_colormap = [[0.0, 'rgb(127, 170, 177)'],[1.0, 'rgb(175, 226, 233)']]
neptune_colormap = [[0.0, 'rgb(47, 53, 137)'],
                    [0.2, 'rgb(52, 71, 165)'],
                    [0.4, 'rgb(56, 90, 185)'],
                    [0.6, 'rgb(61, 121, 209)'],
                    [1.0, 'rgb(158, 189, 253)']]

def sphere(size, position, rotation, texture): 
    N_lat = int(texture.shape[0])
    N_lon = int(texture.shape[1])
    theta = np.linspace(0,2*np.pi,N_lat)
    phi = np.linspace(0,np.pi,N_lon)
    
    # Set up coordinates for points on the sphere
    x0 = size*np.outer(np.cos(theta),np.sin(phi))
    y0 = size*np.outer(np.sin(theta),np.sin(phi))
    z0 = size*np.outer(np.ones(N_lat),np.cos(phi))
    
    # Apply rotation if needed:
    if (rotation == np.eye(3)).all():
        x = x0 + position[0]
        y = y0 + position[1]
        z = z0 + position[2]
    else:
        (N,M) = x0.shape
        verts = rotation@np.stack([x0.flatten(), y0.flatten(), z0.flatten()])
        x = verts[0,:].reshape(N,M) + position[0]
        y = verts[1,:].reshape(N,M) + position[1]
        z = verts[2,:].reshape(N,M) + position[2]
    return x,y,z

def ring(radius, position, rotation, texture):
    N_rad = int(texture.shape[1])
    N_angle = int(texture.shape[0])
    scale = rSaturn/radius
    r = np.linspace(rSaturnRingMin/scale, rSaturnRingMax/scale,N_rad)
    v = np.linspace(0,2*np.pi,N_angle)
    R,V = np.meshgrid(r,v)
    x0 = R*np.cos(V)
    y0 = R*np.sin(V)
    z0 = np.zeros(x0.shape)
    if (rotation == np.eye(3)).all():
        x = x0 + position[0]
        y = y0 + position[1]
        z = z0 + position[2]
    else:
        (N,M) = x0.shape
        verts = rotation@np.stack([x0.flatten(), y0.flatten(), z0.flatten()])
        x = verts[0,:].reshape(N,M) + position[0]
        y = verts[1,:].reshape(N,M) + position[1]
        z = verts[2,:].reshape(N,M) + position[2]
    return x,y,z


def plotly_planets(planet_name: str, position = np.zeros(3), rotation = np.eye(3), 
                                     fig = None, radius: float = None, subsample: int = 10):
    """
    """
    # If now figure is provided, create a new one:
    if fig is None:
        fig = go.Figure()

    if subsample is None:
        subsample = 1

    if planet_name.lower() == "sun":
        stream = pkg_resources.resource_stream('ceres', 'plotting/textures/sun.jpg')
        texture = np.asarray(ImageOps.grayscale(Image.open(stream))).T
        texture = texture[::subsample, ::subsample]
        colorscale = sun_colormap
        if radius is None:
            radius = rSun
            
    elif planet_name.lower() == "mercury":
        stream = pkg_resources.resource_stream('ceres', 'plotting/textures/mercury.jpg')
        texture = np.asarray(ImageOps.grayscale(Image.open(stream))).T
        texture = texture[::subsample, ::subsample]
        colorscale = grey_colormap
        if radius is None:
            radius = rMercury

    elif planet_name.lower() == "venus":
        stream = pkg_resources.resource_stream('ceres', 'plotting/textures/venus.jpg')
        texture = np.asarray(ImageOps.grayscale(Image.open(stream))).T
        texture = texture[::subsample, ::subsample]
        colorscale = venus_colormap
        if radius is None:
            radius = rVenus

    elif planet_name.lower() == "earth":
        stream = pkg_resources.resource_stream('ceres', 'plotting/textures/earth_plotly.jpg')
        texture = np.asarray(Image.open(stream)).T
        texture = texture[1,::subsample, ::subsample]
        colorscale = earth_colormap
        if radius is None:
            radius = rEarth

    elif planet_name.lower() == "moon":
        stream = pkg_resources.resource_stream('ceres', 'plotting/textures/moon.jpg')
        texture = np.asarray(ImageOps.grayscale(Image.open(stream))).T
        texture = texture[::subsample, ::subsample]
        colorscale = grey_colormap
        if radius is None:
            radius = rMoon

    elif planet_name.lower() == "mars":
        stream = pkg_resources.resource_stream('ceres', 'plotting/textures/mars.jpg')
        texture = np.asarray(ImageOps.grayscale(Image.open(stream))).T
        texture = texture[::subsample, ::subsample]
        colorscale = mars_colormap
        if radius is None:
            radius = rMars

    elif planet_name.lower() == "ceres":
        stream = pkg_resources.resource_stream('ceres', 'plotting/textures/ceres.jpg')
        texture = np.asarray(ImageOps.grayscale(Image.open(stream))).T
        texture = texture[::subsample, ::subsample]
        colorscale = grey_colormap
        if radius is None:
            radius = rCeres

    elif planet_name.lower() == "jupiter":
        stream = pkg_resources.resource_stream('ceres', 'plotting/textures/jupiter.jpg')
        texture = np.asarray(ImageOps.grayscale(Image.open(stream))).T
        texture = texture[::subsample,::subsample]
        colorscale = jupiter_colormap
        if radius is None:
            radius = rJupiter

    elif planet_name.lower() == "saturn":
        stream = pkg_resources.resource_stream('ceres', 'plotting/textures/saturn.jpg')
        texture = np.asarray(Image.open(stream)).T
        texture = texture[1,::subsample, ::subsample]
        colorscale = saturn_colormap
        if radius is None:
            radius = rSaturn

        # Create the ring system:
        stream = pkg_resources.resource_stream('ceres', 'plotting/textures/saturn_ring.jpg')
        ring_texture = np.asarray(ImageOps.grayscale(Image.open(stream)))
        x,y,z = ring(radius,position,rotation,ring_texture)
        surf = go.Surface(x=x, y=y, z=z,
                          surfacecolor=ring_texture,
                          colorscale=grey_colormap,
                          showscale=False)
        fig.add_trace(surf)

    elif planet_name.lower() == "uranus":
        stream = pkg_resources.resource_stream('ceres', 'plotting/textures/uranus.jpg')
        texture = np.asarray(ImageOps.grayscale(Image.open(stream))).T
        texture = texture[::subsample, ::subsample]
        colorscale = uranus_colormap
        if radius is None:
            radius = rUranus

    elif planet_name.lower() == "neptune":
        stream = pkg_resources.resource_stream('ceres', 'plotting/textures/neptune.jpg')
        texture = np.asarray(Image.open(stream)).T
        texture = texture[2,::subsample, ::subsample]
        colorscale = neptune_colormap
        if radius is None:
            radius = rNeptune
    else:
        print('No valid plotly_planet named {}'.format(planet_name))
        return None

    x,y,z = sphere(radius,position,rotation,texture)
    surf = go.Surface(x=x, y=y, z=z,
                    surfacecolor=texture,
                    colorscale=colorscale,
                    showscale=False)

    layout = go.Layout(scene=dict(aspectratio=dict(x=1,y=1,z=1)))

    fig.update_layout(layout)
    fig.add_trace(surf)

    return fig


def plotly_mesh(obj, fig=None, name=None, flat_shading=False, show_edges=False):
    """
    """
    # If now figure is provided, create a new one:
    if fig is None:
        fig = go.Figure()     

    # Get the vertices and triangles: 
    verts = obj._vertices
    tris  = obj._triangles
    tri_points = verts[tris]

    x, y, z = verts.T
    I, J, K = tris.T

    pl_mygrey=[0, 'rgb(153, 153, 153)'], [1., 'rgb(255,255,255)']
                            
    pl_mesh = go.Mesh3d(x=x,
                        y=y,
                        z=z,
                        colorscale=pl_mygrey, 
                        intensity= z,
                        flatshading=flat_shading,
                        i=I,
                        j=J,
                        k=K,
                        name=name,
                        showscale=False
                        )

    fig.add_trace(pl_mesh)

    if show_edges:
        Xe = []
        Ye = []
        Ze = []
        for T in tri_points:
            Xe.extend([T[k%3][0] for k in range(4)]+[ None])
            Ye.extend([T[k%3][1] for k in range(4)]+[ None])
            Ze.extend([T[k%3][2] for k in range(4)]+[ None])
            
        #define the trace for triangle sides
        lines = go.Scatter3d(
                        x=Xe,
                        y=Ye,
                        z=Ze,
                        mode='lines',
                        name='',
                        line=dict(color= 'rgb(70,70,70)', width=1))
        fig.add_trace(lines)

    return fig



def plotly_random_color():
    """
    """
    return 'rgb({},{},{})'.format(np.random.randint(0,256),np.random.randint(0,256),np.random.randint(0,256))


def plotly_light(fig):
    """
    """


def plotly_axisequal(fig):
    """
    """
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

    trace = go.Scatter3d(x=orbit[0,:].flatten(), y=orbit[1,:].flatten(), z=orbit[2,:].flatten(),name=name,
                         marker=dict(size=0.1), line=dict(color=line_color, width=line_width))

    # Add trace to the figure:
    fig.add_trace(trace)

    return fig