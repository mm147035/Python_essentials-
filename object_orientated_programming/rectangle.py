# This program defines a class for a Rectangle and calculates its area and perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Create an instance of the Rectangle class
rectangle = Rectangle(5, 10)

# Calculate the area and perimeter of the rectangle
print("The area of the rectangle is:", rectangle.area())
print("The perimeter of the rectangle is:", rectangle.perimeter())