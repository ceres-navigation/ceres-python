from ceres.models.gravity import GravityField, PointMass
from ceres.constants import muEarth, rEarth
import numpy as np

def test_models_pointmass():
    pm = PointMass(muEarth)
    position = rEarth*np.array([1,0,0])
    assert np.linalg.norm(pm.get_acceleration(position)) == 0.009820224591618645


test_models_pointmass()