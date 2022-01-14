from ceres.gravity import PointMass
from ceres.constants import muEarth,rEarth
import numpy as np

def main():
    earth_gravity = PointMass(muEarth)
    accel = earth_gravity.get_acceleration(rEarth*np.array([1,0,0]))
    surface_gravity = np.linalg.norm(accel)
    print(surface_gravity)

if __name__ == "__main__":
    main()