"""
"""

from ceres.spiceutils import time_to_et


class MeasurementEvent:
    """
    """
    def __init__(self, sensor, measurement_type, target):
        """
        """
        self._sensor = sensor
        self._measurement_type = measurement_type
        self._target = target
        self._measurement = None

    def execute(self,dynamics):
        """
        """
        self._measurement = self._sensor.measurement(self._measurement_type, self._target)

class ManeuverEvent:
    """
    """
    # TODO: THIS IS NOT FULLY THOUGHT OUT YET.  DOES NOT WORK
    def __init__(self, thruster, burn):
        self._thruster = thruster
        self._burn = burn
    
    def execute(self):
        self._actuator.burn(self._burn)

class StartEvent:
    """
    """
    def __init__(self):
        pass

class EndEvent:
    """
    """
    def __init__(self):
        pass


class EventsPlan:
    """
    """
    def __init__(self, start, end):
        """
        """
        start = time_to_et(start)
        end   = time_to_et(end)
        self._events = [[start, [StartEvent()]],
                        [ end,  [EndEvent()]  ]]

    def add_measurement_plan(self, times, sensor, measurement_type: str, target):
        """
        """
        times = time_to_et(times)

        for time in times:
            index = None
            for idx, event in enumerate(self._events):
                if time == event[0]:
                    index = idx
                    break
            if index is None:
                self._events.append([time, [MeasurementEvent(sensor, measurement_type, target)]])
            else:
                self._events[index][1].append(MeasurementEvent(sensor, measurement_type, target))


        # Sort the events list by the time stamps
        self._events.sort(key=lambda x: float(x[0]))


    def __iter__(self):
        """
        """
        return EventsIterator(self)

    def __getitem__(self, item):
        """
        """
        return self._events[item]
        
    def __len__(self):
        """
        """
        return len(self._events)


class EventsIterator:
    """
    """
    def __init__(self, events):
        """
        """
        self._events = events
        self._index = 0

    def __next__(self):
        """
        """
        if self._index < len(self._events._events):
            self._index = self._index + 1
            return self._events._events[self._index-1]
        raise StopIteration