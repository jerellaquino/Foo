import sys
import os
import unittest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from foo_package.foo import sphereVolume, sphereSA

class TestSphereCalc(unittest.TestCase):

    # Check different function input types:
    
    def test_sphereVolume(self):
        self.assertAlmostEqual(sphereVolume(4), 268.08, places=2)
        self.assertAlmostEqual(sphereVolume(3.14159264), 129.87879, places=5)
        self.assertEqual(sphereVolume("hi"), 'error: check radius input value, must be integer or float')


    def test_sphereSA(self):
        self.assertAlmostEqual(sphereSA(2), 50.27, places=2)
        self.assertAlmostEqual(sphereSA(3.14159264), 124.02511, places=5)
        self.assertEqual(sphereSA("hi"), 'error: check radius input value, must be integer or float')


if __name__ == '__main__':
    unittest.main()