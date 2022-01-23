"""
"""
from typing import Union, List, Optional
import numpy as np
from ceres.sensors.antenna_patterns import Isotropic
from ceres import Component

class Antenna(Component):
    """
    """
    def __init__(self, pattern = Isotropic, **kwds):
        """
        """
        super().__init__(**kwds)

        self._pattern = pattern


class Radio:
    """
    """
    def __init__(self, frequency: float, antennas: Union[Antenna, List[Antenna]], obstacles = None,
                 lt_delay: bool = False):
        """
        """
        self._frequency = frequency

        if type(antennas) is Antenna:
            self._antennas = [antennas]

        elif type(antennas) is list:
            self._antennas = antennas

        else:
            # TODO: Error handle?
            print('Radio must be provided ')

        self._doppler_events = []
        self._range_events = []
        self._obstacles = obstacles
        self._lt_delay = lt_delay

    def set_parent(self, parent_obj):
        """
        """
        for antenna in self._antennas:
            antenna.set_parent(parent_obj)

    def event(self, event_type, target_radio):
        """
        """
        if event_type.lower() == 'doppler':
            return self.doppler(target_radio)
        elif event_type.lower() == 'range':
            return self.range(target_radio)

    def doppler(self, target_radio):
        """
        """
        # for antenna in self._antennas:
            
        # return doppler_measurement
        return

    def range(self, target_radio):
        """
        """
        return range