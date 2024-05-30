#calc_functions
#
# Description:
#    functions for foo physics calculations!
#    you can add more functions in the future for new science features  

import math

#  function to calculate volume of a sphere
def sphereVolume(radius):
 volume = 4/3 * math.pi * radius ** 3
 return volume

# function to calculate surface area of sphere

def sphereSA(radius):
    surfaceArea = 4 * math.pi * radius ** 2
    return surfaceArea