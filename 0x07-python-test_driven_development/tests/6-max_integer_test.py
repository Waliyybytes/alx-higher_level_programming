#!/usr/bin/python3
"""
	A unittest for max_integer([..]) function
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """class definition inheriting from unittest.TestCase"""
    def test_module_docstring(self):
        """Checks for module doc"""
        mdl = __import__('6-max_integer').__doc__
        self.assertTrue(len(mdl) > 1)

    def test_function_docstring(self):
        """Tests for function doc"""
        func = max_integer.__doc__
        self.assertTrue(len(func) > 1)

    def test_max_integer(self):
        """ Test the maximum for normal integers"""
        self.assertEqual(max_integer([1, -5, 1/5, 17/2]), 17/2)

    def test_types(self):
        """ Tests the values in the list"""
        self.assertRaises(TypeError, max_integer, [1, -5, 1/7, False])

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Tests for a non-int type in list"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)
        
if __name__ == "__main__":
    unittest.main()
