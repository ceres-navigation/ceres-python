"""
"""
def rk4(dynamics, dt, X, *argv):
    """
    """
    k1 = dt*dynamics(0, X, *argv)
    k2 = dt*dynamics(0.5*dt, X + 0.5*k1, *argv)
    k3 = dt*dynamics(0.5*dt, X + 0.5*k2, *argv)
    k4 = dt*dynamics(dt, X + k3, *argv)

    return X + (1/6)*(k1 + 2*k2 + 2*k3 + k4)