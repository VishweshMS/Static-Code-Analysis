# -*- coding: utf-8 -*-
"""
Updated Feb 10, 2023
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Vishwesh Malur Somashekar

"""

import unittest

from triangle import classify_triangle,my_brand

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
    def testequilateraltriangle_a(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(5,5,5),'Equilateral','5,5,5 should be equilateral')

    def test_equilateral_triangle_b(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(33,33,33),'Equilateral','33,33,33 should be equilateral')

    def testequilateraltrianglec(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(6,6,6),'Equilateral','6,6,6 should be equilateral')

    def testisoscelestrianglea(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(8,10,10),'Isosceles','8,10,10 is a Isosceles Triangle')

    def testisoscelestriangleb(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(12, 14, 14),'Isosceles','12, 14, 14 is Isosceles')

    def testisoscelesirianglec(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(9, 6, 9),'Isosceles','9, 6, 9 is a Isosceles Triangle')

    def testscalenetrianglea(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(12, 15, 20),'Scalene','12, 15, 20 is a Scalene')

    def testscalenetriangleb(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(25, 30, 35),'Scalene','25, 30, 35 is Scalene')

    def testscalenetrianglec(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(40, 45, 55),'Scalene','40, 45, 55 is a Scalene Triangle')

    def testrighttrianglea(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(9, 12, 15),'Right','9, 12, 15 is a Right triangle')

    def testrighttriangleb(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(5, 12, 13),'Right','5, 12, 13 should be Right Triangle')

    def testrighttrianglec(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(8, 15, 17),'Right','8, 15, 17 should be Right Triangle')

    def testnotatrianglea(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(6,8,15),'NotATriangle','6,8,15 not a Triangle')

    def testnotatriangleb(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(10,11,21),'NotATriangle','10,11,21 not a Triangle')

    def testnotatrianglec(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(9,13,22),'NotATriangle','9,13,22 cannot form a Triangle')

    def testinvaliddataa(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(-1, 2, 3),'InvalidInput','-1, 2, 3 is a Invalid Data')

    def testinvaliddatab(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(1.1, 2, 3),'InvalidInput','1.1, 2, 3 is a Invalid Data')

    def testinvaliddatac(self):
        """
    This is a docstring for my_function.
    
    Parameters:
    parameter1 (type): Description of parameter1.
    parameter2 (type): Description of parameter2.
    
    Returns:
    return_value (type): Description of the return value.
    """
        self.assertEqual(classify_triangle(0, 0, 1),'InvalidInput','0, 0, 1 is a Invalid Data')


if __name__ == '__main__':
    my_brand("HW 02A")
    print('Running unit tests')
    unittest.main()
    