import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(None)
        self.assertEqual(10, max_list_iter([3, 2, 5, 6, 2, 6, 8, 10]))
        self.assertEqual(5, max_list_iter([5]))
        self.assertEqual(6, max_list_iter([5, 6]))
        self.assertEqual(9, max_list_iter([9, 6, 0]))
        self.assertEqual(None, max_list_iter([]))

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([1, 3, 6, 2]), [2, 6, 3, 1])
        self.assertEqual(reverse_rec([]), [])
        self.assertEqual(reverse_rec([5]), [5])
        with self.assertRaises(ValueError):
            reverse_rec(None)

    def test_bin_search(self):
        with self.assertRaises(ValueError):
            bin_search(3, 5, 6, None)

        self.assertEqual(None, bin_search(7, 0, 0, []))
        self.assertEqual(None, bin_search(7, 0, 0, [2]))
        self.assertEqual(0, bin_search(2, 0, 0, [2]))
        self.assertEqual(None, bin_search(6, 3, 5, [2, 6, 8, 8, 32, 531]))

        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1

        self.assertEqual(4, bin_search(4, low, high, list_val))
        self.assertEqual(0, bin_search(0, low, high, list_val))
        self.assertEqual(5, bin_search(7, low, high, list_val))
        self.assertEqual(high, bin_search(10, low, high, list_val))
        self.assertEqual(None, bin_search(32, low, high, list_val))
        self.assertEqual(None, bin_search(5, low, high, list_val))
        self.assertEqual(None, bin_search(-235, low, high, list_val))


if __name__ == "__main__":
    unittest.main()
