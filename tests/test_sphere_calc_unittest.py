import unittest
from foo import sphereVolume, sphereSA

class TestSphereCalc(unittest.TestCase):

    def test_sphereVolume(self):
        self.assertAlmostEqual(sphereVolume(4), 268.08, places=2)

    def test_sphereSA(self):
        self.assertAlmostEqual(sphereSA(2), 50.27, places=2)

if __name__ == '__main__':
    unittest.main()