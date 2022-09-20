#!/usr/bin/python3
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """class definition inheriting from unittest.TestCase"""

    def test_max_integer(self):
        """ Test the maximum for normal integers"""
        self.assertEqual(max_integer([1, -5, 1/5, 17/2]), 17/2)

    def test_types(self):
        """ Tests the values in the list"""
        self.assertRaises(TypeError, max_integer, [1, -5, 1/7, False])
