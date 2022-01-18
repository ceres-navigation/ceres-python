"""
The :mod:`constants` module defines constants useful in simulating spacecraft navigation systems.  These constants are things such as the standard gravitational parameters :math:`(\mu)` and radii of notable celestial bodies, as well as some useful universal constants.

For example, if the conversion from Astronomical Units to km as well as the standard graviational parameter of the Sun were needed, they could be imported using the following:

.. code-block:: python

   from ceres.constants import AU, muSun

.. warning::

   These values are intended to be easily accesible for prototyping purposes and not intended for operational use.  While they may be acceptable, it is recommended you look for specific data products related to your specific needs.
"""
#: Speed of light :math:`(\frac{km}{s})`
c = 299792458/1000

#: Gravitational Constant :math:`(\frac{km^3}{kg\cdot s^2})`
G = (6.67430E-11)/(1000**3)

#: Astronomical Unit :math:`(km)`
AU = 149597870.700

#: Seconds per day
SPD  = 86400

#: Seconds per sideral day
SPSD = 23*3600 + 56*60 + 4.1

#: :math:`\mu_{Sun}` :math:`(\frac{km^3}{s^2})`
muSun     = (1.32712440018E20)/(1000**3)

#: Solar radius :math:`(km)`
rSun     = 695508

#: :math:`\mu_{mercury}` :math:`(\frac{km^3}{s^2})`
muMercury = (2.2032E13)/(1000**3)

# Mercury radius :math:`(km)`
rMercury = 2439.4

#: :math:`\mu_{venus}` :math:`(\frac{km^3}{s^2})`
muVenus   = (3.24859E14)/(1000**3)

# Venus radius :math:`(km)`
rVenus   = 6052

#: :math:`\mu_{earth}` :math:`(\frac{km^3}{s^2})`
muEarth   = (3.986004418E14)/(1000**3)

#: Earth radius :math:`(km)`
rEarth   = 6371.0084

#: :math:`\mu_{moon}` :math:`(\frac{km^3}{s^2})`
muMoon    = (4.9048695E12)/(1000**3)

#: Lunar radius :math:`(km)`
rMoon    = 1737.5

#: :math:`\mu_{mars}` :math:`(\frac{km^3}{s^2})`
muMars    = (4.282837E13)/(1000**3)

#: Mars radius :math:`(km)`
rMars    = 3389.5

#: :math:`\mu_{ceres}` :math:`(\frac{km^3}{s^2})`
muCeres   = (6.26325E10)/(1000**3)

#: Ceres radius :math:`(km)`
rCeres   = 469.7

#: :math:`\mu_{jupiter}` :math:`(\frac{km^3}{s^2})`
muJupiter = (1.26686534E17)/(1000**3)

#: Jupiter radius :math:`(km)`
rJupiter = 69911

#: :math:`\mu_{saturn}` :math:`(\frac{km^3}{s^2})`
muSaturn  = (3.7931187E16)/(1000**3)

#: Saturn radius :math:`(km)`
rSaturn  = 58232

#: Saturn ring inner radius :math:`(km)`
rSaturnRingMin = 66900

#: Saturn ring outter radius :math:`(km)`
rSaturnRingMax = 136780

#: :math:`\mu_{uranus}` :math:`(\frac{km^3}{s^2})`
muUranus  = (5.793939E15)/(1000**3)

#: Uranus radius :math:`(km)`
rUranus  = 25362

#: :math:`\mu_{neptune}` :math:`(\frac{km^3}{s^2})`
muNeptune = (6.836529E15)/(1000**3)

#: Neptune radius :math:`(km)`
rNeptune = 24622