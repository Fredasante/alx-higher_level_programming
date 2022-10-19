#!/usr/bin/python3
"""Unittest for the max_integer module."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase Class for the max_integer function."""

    def testmax(self):
        """Test to see the function work as it should."""
        a = [1, 2, 3, 4]
        res = max_integer(a)
        self.assertEqual(res, 4)

    def test_not_int(self):
        """Test with strings and ints combined."""
        a = ['H', 9, 'String']
        self.assertRaises(TypeError, max_integer, a)

    def test_None(self):
        """Test with 'None' as parameter."""
        a = None
        self.assertRaises(TypeError, max_integer, a)

    def test_empty(self):
        """Test with empty list."""
        a = []
        res = max_integer(a)
        self.assertEqual(res, None)

    def test_floats(self):
        """Test with a list of floats."""
        a = [9.8, 7.9]
        res = max_integer(a)
        self.assertEqual(res, 9.8)

    def test_negatives(self):
        """Test with negative integers."""
        a = [-80, -72, -71]
        res = max_integer(a)
        self.assertEqual(res, -71)

    def test_not_list(self):
        """Test with string parameter."""
        a = "String"
        res = max_integer(a)
        self.assertEqual(res, 't')

    def test_only_num(self):
        """Test with list with only one integer."""
        a = [9]
        res = max_integer(a)
        self.assertEqual(res, 9)

    def test_strings(self):
        """Test with a list of strings."""
        a = ['holiday', 'holey']
        res = max_integer(a)
        self.assertEqual(res, 'holiday')

    def test_repeat_nums(self):
        """Test with list of identical numbers."""
        a = [2, 2, 2, 2]
        res = max_integer(a)
        self.assertEqual(res, 2)

    def test_mixed(self):
        """Test with a  list of ints and floats."""
        a = [1.2, 7, 9.2, 3]
        res = max_integer(a)
        self.assertEqual(res, 9.2)


if __name__ == '__main__':
    unittest.main()
