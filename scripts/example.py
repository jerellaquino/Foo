# Examples of how to import functions and using them
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from foo_package.foo import sphereVolume, sphereSA

print("test sphereVolume: radius = 2\n    result:", sphereVolume(2))

print("test sphereSA: radius = 2\n    result:", sphereSA(2))
