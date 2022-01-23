"""
"""
from typing import Optional
import numpy as np

from ceres.spiceutils import time_to_et
from ceres.events import EventsPlan

class FilterScene:
    """
    """

class TruthScene:
    """
    """
    def __init__(self, dynamics, objects: list, events_plan: EventsPlan):
        """
        """
        # Convert start and stop times into ephemeris times:
        self._dynamics = dynamics
        self._objects = objects
        self._events_plan = events_plan

    def simulate(self, dt_base: float = 30):
        """
        """
        # Create the timespan:
        event_times = [events[0] for events in self._events_plan]
        tspan = np.arange(event_times[0], event_times[-1], dt_base).tolist()
        tspan = tspan + event_times
        tspan = list(set(tspan))
        tspan.sort()
        self._tspan = tspan

        # Prepare objects for logging data:
        for object in self._objects:
            object.preallocate(len(self._tspan))

        # Enter the main simulation loop:
        idx = 0
        for event_time, events in self._events_plan[1:]:
            if idx != 0 :
                dt = (event_time - start_time)/np.ceil((event_time - start_time)/dt_base)
                tspan_to_next_event = np.arange(start_time, event_time-dt, dt)
                for tstep in tspan_to_next_event:
                    # Propagate the dynamics by the current time step:
                    self._dynamics(tstep, dt, self._objects)

                    # Log for the current time step:
                    for object in self._objects:
                        object.log(idx, tstep+dt)
                    idx = idx+1
                tstep = tstep+dt

            # Process the event:
            for event in events:
                complete = False
                while not complete:
                    dt, complete = event.execute()
                    self._dynamics(tstep, dt, self._objects)

            start_time = event_time

