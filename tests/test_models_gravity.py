from ceres.models.gravity import GravityField, PointMass
from ceres.constants import muEarth, rEarth
import numpy as np


def test_models_pointmass():
    # Test the get acceleration method:
    pm = PointMass(muEarth)
    position = rEarth*np.array([1,0,0])
    assert np.linalg.norm(pm.get_acceleration(position)) == 0.009820224591618645

    # Test the set_position method:
    position = np.array([1,2,3])
    pm.set_position(position)
    assert (pm._position == position).all()

test_models_pointmass()