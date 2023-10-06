# Exercise 1: Create a function that calculates the area of different shapes. 
# The function should take the shape type and its parameters as inputs.

def calculate_area(shape, *args):
    # Your code here
    import math
    if shape == "square":
        return args[0]* args[0]
    if shape == "rectangle":
        return args [0]* args [1]
    if shape == "triangle":
        return args [0]* args [1]/2
    if shape =="circle":
        return round(args[0]* args[0]*math.pi,2)
# Unit tests
import unittest

class TestExercise1(unittest.TestCase):

    def test_calculate_area(self):
        self.assertEqual(calculate_area("square", 4), 16)
        self.assertEqual(calculate_area("rectangle", 4, 7), 28)
        self.assertEqual(calculate_area("triangle", 3, 6), 9)
        self.assertEqual(calculate_area("circle", 3), 28.27)

if __name__ == '__main__':
    unittest.main()
