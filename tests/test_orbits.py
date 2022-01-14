from ceres.orbits import TwoBody
from ceres.constants import muSun

def test_twobody():
    a = 1
    e = 1
    i = 1
    w = 1
    W = 1
    ma = 1
    orbit = TwoBody(muSun,a=a,e=e,i=i,w=w,W=W,ma=ma)