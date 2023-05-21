# This program defines a class for a Circle and calculates its area and circumference.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius

# Create an instance of the Circle class
circle = Circle(5)

# Calculate the area and circumference of the circle
print("The area of the circle is:", circle.area())
print("The circumference of the circle is:", circle.circumference())
