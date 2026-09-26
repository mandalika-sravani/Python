# super() --- Function used in a child class to call methods from a parent class (super class). 
#               Allows to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

cicrle = Circle("Red", True, 10)
square = Square("Blue", True, 12)
tri = Triangle("Yellow", False, 10, 15)

print(cicrle.color)
print(square.width)
