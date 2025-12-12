import math
''' 
 Import the `math` module to use mathematical constants and functions
 in this case we use `math.pi` for the value of π and `math.pow()` for raising powers.

 -----------------------------
 Base (abstract) class Shape
 -----------------------------
''' 
class Shape:
    '''
     This class acts as an "interface" or abstract class.
     Defines the `calculateArea()` method that any subclass must implement.
     We don't implement the logic here; instead we raise an exception to
     force subclasses to provide their own implementation.
    '''
    def calculateArea(self):
        raise NotImplementedError("Subclass must implement calculateArea()")
    ''' 
         NotImplementedError is a way to indicate that this method is abstract:
         if someone creates a class that inherits from Shape and doesn't override calculateArea,
         calling calculateArea() will trigger this error.
    '''
'''
 -----------------------------
 Circle class (inherits from Shape)
 -----------------------------
'''
class Circle(Shape):
    def __init__(self, radius):
        '''
         Save the radius as an internal attribute. By convention we use _radius
         to indicate it's for internal use (encapsulation by convention).
        '''
        self._radius = radius

    def calculateArea(self):
        '''
         Circle area formula: π * r^2
         math.pi is π and math.pow(self._radius, 2) raises the radius to the power of 2.
         Returns a number (float).
        '''
        return math.pi * math.pow(self._radius, 2)
'''
 -----------------------------
 Square class (inherits from Shape)
 -----------------------------
'''
class Square(Shape):
    def __init__(self, side):
        # Save the side of the square
        self._side = side

    def calculateArea(self):
        # Square area: side^2
        return math.pow(self._side, 2)
        # Equivalent alternative: return self._side ** 2
'''
 -----------------------------
 Rectangle class (inherits from Shape)
 -----------------------------
'''
class Rectangle(Shape):
    def __init__(self, base, height):
        # Save base and height as internal attributes
        self._base = base
        self._height = height

    def calculateArea(self):
        # Rectangle area: base * height
        return (self._base * self._height)
'''
 -----------------------------
 Triangle class (inherits from Shape)
 -----------------------------
'''
class Triangle(Shape):
    def __init__(self, base, height):
        # Save base and height of the triangle
        self._base = base
        self._height = height

    def calculateArea(self):
        # Triangle area: (base * height) / 2
        return (self._base * self._height) / 2
'''
 -----------------------------
 Creating instances (polymorphism)
 -----------------------------
 Here we create a list with objects from different Shape subclasses.
 All classes inherit from Shape and therefore have the calculateArea method.
'''
shapes = [
    Circle(5),        # circle with radius 5
    Square(10),      # square with side 10
    Rectangle(7, 3),  # rectangle with base 7 and height 3
    Triangle(4, 6)    # triangle with base 4 and height 6
]
'''
 -----------------------------
 Polymorphic use of calculateArea()
 -----------------------------
'''
for shape in shapes:
    '''
     We don't need to know the specific type of `shape` here.
     We call the same method `calculateArea()` and Python will choose
     the appropriate implementation based on the object's class (dynamic dispatch).
    '''
    area = shape.calculateArea()
    '''
     We print the area. Here we show how each subclass responds differently
     to the same message (calculateArea) — that's polymorphism.
    '''
    print(f"Area: {area}")
