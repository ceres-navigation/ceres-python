"""
"""
from typing import Optional
import numpy as np

from ceres.spiceutils import time_to_et

class Scene:
    """
    """
    def __init__(self, dynamics, objects: list, time_span: list, events: Optional[list] = None):
        """
        """
        # Convert start and stop times into ephemeris times:
        self._dynamics = dynamics
        self._objects = objects
        self._events = events
        self._et_start = time_to_et(time_span[0])
        self._et_end   = time_to_et(time_span[1])

        # Process the events list:
        # TODO: Use pandas datetime arrays... maybe just time_to_et again?


    def simulate(self, max_stepsize: float = 10, min_stepsize: float = 0):
        """
        """
        # TODO: Add adaptive step size...
        dt = max_stepsize

        # Create the timespan:
        # TODO: This needs to include events (start and end of event, so an additional 2N
        # entries need to be added for N items in the event list
        self._tspan = np.arange(self._et_start, self._et_end, dt)

        # Prepare objects for logging data:
        for object in self._objects:
            object.preallocate(self._tspan.size)

        # Enter the main simulation loop:
        for idx, tstep in enumerate(self._tspan):
            #TODO: Have this main simulation loop handle events

            self._dynamics(tstep, dt, self._objects)

            for object in self._objects:
                object.log(idx, tstep)



