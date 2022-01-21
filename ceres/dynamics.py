"""
"""
def rk4(dynamics, dt, X, *argin):
    """
    """
    k1 = dt*dynamics(0, X, argin)
    k2 = dt*dynamics(0.5*dt, X + 0.5*k1, argin)
    k3 = dt*dynamics(0.5*dt, X + 0.5*k2, argin)
    k4 = dt*dynamics(dt, X + k3, argin)

    return X + (1/6)*(k1 + 2*k2 + 2*k3 + k4)

def simple_orbit():
    """
    """
    