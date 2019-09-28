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
        self.assertEqual(10, max_list_iter([10, 10, 2, 2]))
        self.assertEqual(None, max_list_iter([]))

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([1, 3, 6, 2]), [2, 6, 3, 1])
        self.assertEqual(reverse_rec([]), [])
        self.assertEqual(reverse_rec([5, 3]), [3, 5])
        self.assertEqual(reverse_rec([5]), [5])
        with self.assertRaises(ValueError):
            reverse_rec(None)

    def test_bin_search(self):
        duplicate_list = [0, 2, 5, 5, 6, 7, 10, 10]
        found_index = bin_search(5, 0, 7, duplicate_list)
        self.assertEqual(5, duplicate_list[found_index])

        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        high = len(list_val) - 1

        self.assertEqual(4, bin_search(4, 4, 4, list_val))
        self.assertEqual(None, bin_search(3, 4, 4, list_val))
        self.assertEqual(4, bin_search(4, 0, high, list_val))
        self.assertEqual(0, bin_search(0, 0, high, list_val))
        self.assertEqual(5, bin_search(7, 0, high, list_val))
        self.assertEqual(high, bin_search(10, 0, high, list_val))
        self.assertEqual(None, bin_search(1, 0, 1, [0, 2]))
        self.assertEqual(None, bin_search(1, 0, 2, [0, 2, 2]))

    def test_bin_search_small_n(self):
        self.assertEqual(None, bin_search(32, 0, 0, []))
        self.assertEqual(0, bin_search(2, 0, 0, [2]))

        self.assertEqual(0, bin_search(0, 0, 1, [0, 1]))
        self.assertEqual(1, bin_search(1, 0, 1, [0, 1]))

        self.assertEqual(0, bin_search(0, 0, 2, [0, 1, 2]))
        self.assertEqual(1, bin_search(1, 0, 2, [0, 1, 2]))
        self.assertEqual(2, bin_search(2, 0, 2, [0, 1, 2]))

        self.assertEqual(0, bin_search(0, 0, 3, [0, 1, 2, 3]))
        self.assertEqual(1, bin_search(1, 0, 3, [0, 1, 2, 3]))
        self.assertEqual(2, bin_search(2, 0, 3, [0, 1, 2, 3]))
        self.assertEqual(3, bin_search(3, 0, 3, [0, 1, 2, 3]))

        self.assertEqual(0, bin_search(0, 0, 4, [0, 1, 2, 3, 4]))
        self.assertEqual(1, bin_search(1, 0, 4, [0, 1, 2, 3, 4]))
        self.assertEqual(2, bin_search(2, 0, 4, [0, 1, 2, 3, 4]))
        self.assertEqual(3, bin_search(3, 0, 4, [0, 1, 2, 3, 4]))
        self.assertEqual(4, bin_search(4, 0, 4, [0, 1, 2, 3, 4]))

        self.assertEqual(0, bin_search(0, 0, 5, [0, 1, 2, 3, 4, 5]))
        self.assertEqual(1, bin_search(1, 0, 5, [0, 1, 2, 3, 4, 5]))
        self.assertEqual(2, bin_search(2, 0, 5, [0, 1, 2, 3, 4, 5]))
        self.assertEqual(3, bin_search(3, 0, 5, [0, 1, 2, 3, 4, 5]))
        self.assertEqual(4, bin_search(4, 0, 5, [0, 1, 2, 3, 4, 5]))
        self.assertEqual(5, bin_search(5, 0, 5, [0, 1, 2, 3, 4, 5]))

    def test_bin_search_errors(self):
        # High exceeds range
        with self.assertRaises(AssertionError):
            bin_search(10, 3, 6, [0, 1, 2, 3, 4, 5])

        # Low is negative
        with self.assertRaises(AssertionError):
            bin_search(10, -1, 5, [0, 1, 2, 3, 4, 5])

        # List is None
        with self.assertRaises(ValueError):
            bin_search(3, 5, 6, None)

    def test_bin_search_not_exists(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        high = len(list_val) - 1

        self.assertEqual(None, bin_search(32, 0, high, list_val))
        self.assertEqual(None, bin_search(5, 0, high, list_val))
        self.assertEqual(None, bin_search(-235, 0, high, list_val))

        self.assertEqual(None, bin_search(7, 0, 0, []))
        self.assertEqual(None, bin_search(7, 0, 0, [2]))
        self.assertEqual(None, bin_search(6, 3, 5, [2, 6, 8, 8, 32, 531]))


if __name__ == "__main__":
    unittest.main()
