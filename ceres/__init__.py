"""Hello from the future
"""

__version__ = '0.0.1a8'

from .keplerorbit import *
from .rigidbody import RigidBody, CelestialBody, Spacecraft
from .rotation import *
from .dynamics import rk4, simple_orbit
from .scene import Scene
