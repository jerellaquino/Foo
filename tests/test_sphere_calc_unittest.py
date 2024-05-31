import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from foo_package.foo import sphereVolume, sphereSA

class TestSphereCalc(unittest.TestCase):

    def test_sphereVolume(self):
        self.assertAlmostEqual(sphereVolume(4), 268.08, places=2)

    def test_sphereSA(self):
        self.assertAlmostEqual(sphereSA(2), 50.27, places=2)

if __name__ == '__main__':
    unittest.main()