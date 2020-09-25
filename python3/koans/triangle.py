#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE

    # Check that the triangle is valid
    if not is_valid_triangle(a, b, c):
        raise TriangleError("The values {0}, {1}, and {2} do not make a valid triangle".format(a, b, c))

    # Since sets essentially trim down to unique values, by putting 
    # the values into a set and checking the length, we can see what 
    # type of triangle it is.
    triangle_set = set([a, b, c])
    if len(triangle_set) == 1:
        return "equilateral"
    elif len(triangle_set) == 2:
        return "isosceles"
    else:
        return "scalene"

def is_valid_triangle(a, b, c):
    
    side_list = [a, b, c]

    # Iterate through the list and insure all the values are greater than 0.
    for side in side_list:
        if side <= 0:
            return False

    # Check that any two sides are always greater than the third.
    side_total = a + b + c
    for side in side_list:
        if side > side_total - side:
            return False 

    # If we get here, the triangle is valid
    return True

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
