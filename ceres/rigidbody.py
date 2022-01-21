import numpy as np
from typing import Union, Sequence, Optional

from ceres.gravity import GravityField
from ceres.spiceutils import SpiceOrbit, SpiceRotation

class RigidBody():
    """
    """
    def __init__(self, et: float = 0,
                       state: Union[Sequence, np.ndarray, SpiceOrbit] = np.zeros(6), 
                       rotation: Union[np.ndarray, SpiceRotation] = np.eye(3),
                       sensors: list = []):
        """
        """
        self._et = et

        self._sensors = sensors
        for sensor in self._sensors:
            sensor.set_parent(self)

        self._state_calc = []
        self._state_calc_et = []
        self._rotation_calc = []
        self._rotation_calc_et = []

        if type(state) is SpiceOrbit:
            self._state_fun = state
            self._state = self._state_fun.states(self._et)
            self._state_calc.append(self._state)
            self._state_calc_et.append(self._et)
        else:
            self._state_fun = None
            state = np.asarray(state)
            self._state = state.reshape((6,1))

        if type(rotation) is SpiceRotation:
            self._rotation_fun = rotation
            self._rotation = self._rotation_fun.rotation(self._et)
            self._rotation_calc.append(self._rotation)
            self._rotation_calc_et.append(self._et)
        else:
            self._rotation_fun = None
            self._rotation = np.asarray(rotation)

    def state(self, dt: Optional[float] = 0):
        """
        """
        if self._state_fun is None:
            return self._state
        else:
            new_et = self._et + dt
            if new_et not in self._state_calc_et:
                self._state_calc.append(self._state_fun.states(new_et))
                self._state_calc_et.append(new_et)
            return self._state_calc[self._state_calc_et.index(new_et)]

    def rotation(self, dt: Optional[float] = 0):
        """
        """
        if self._rotation_fun is None:
            return self._rotation
        else:
            new_et = self._et + dt
            if new_et not in self._rotation_calc_et:
                self._rotation_calc.append(self._rotation_fun.rotation(new_et))
                self._rotation_calc_et.append(new_et)
            return self._rotation_calc[self._rotation_calc_et.index(new_et)]

    def set_state(self, state):
        self._state = state

    def set_rotation(self, rotation):
        self._rotation = rotation

    @property
    def et(self):
        """
        """
        return self._et

    def update_et(self, et: float):
        """
        """
        self._state_calc = []
        self._state_calc_et = []
        self._rotation_calc = []
        self._rotation_calc_et = []
        self._et = et

    def add_to_plot(self, fig):
        """
        """
        return 

    def preallocate(self, num_steps):
        """
        """
        self._time = np.zeros(num_steps)
        self._state_log = np.zeros((6,1,num_steps))
        self._rotation_log = np.zeros((3,3,num_steps))

    def log(self,idx,tstep):
        self._time[idx] = tstep
        self._state_log[:,:,idx] = self._state
        self._rotation_log[:,:,idx] = self._rotation
        

class CelestialBody(RigidBody):
    """
    """
    def __init__(self, gravity: Optional[GravityField] = None, **kwds):
        # TODO: >>> PointMass is GravityField -> False....  figure out how to approach this
        super().__init__(**kwds)
        self._gravity = gravity
        self._gravity.set_parent(self)

    @property
    def gravity(self):
        return self._gravity



class Spacecraft(RigidBody):
    """
    """
    def __init__(self, actuators: list = [], **kwds):
        super().__init__(**kwds)
        return