import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")

    # Add more tests!
    def test_equal(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = Location("SLO", 35.3, -120.7)
        loc4 = loc1

        self.assertTrue(loc1 == loc1)
        self.assertTrue(loc1 == loc4)
        self.assertTrue(loc1 == loc3)
        self.assertTrue(loc1 != loc2)
        self.assertTrue(loc4 != loc2)


if __name__ == "__main__":
    unittest.main()
