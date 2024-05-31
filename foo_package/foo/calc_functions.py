#calc_functions
#
# Description:
#    functions for foo physics calculations!
#    you can add more functions in the future for new science features  

import math

#  function to calculate volume of a sphere
def sphereVolume(radius):
 if ((type(radius) is int) or (type(radius) is float)):
    volume = 4/3 * math.pi * radius ** 3
    return volume
 else: 
    return "error: check radius input value, must be integer or float"

# function to calculate surface area of sphere
def sphereSA(radius):
    if ((type(radius) is int) or (type(radius) is float)):
        surfaceArea = 4 * math.pi * radius ** 2
        return surfaceArea
    else: 
        return "error: check radius input value, must be integer or float"