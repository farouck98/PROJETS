from shape import Shape
from math import pi
class Circle(Shape):
    def __init__(self, rayon:float):
       self.rayon= rayon
    def area(self):
        return 2 * pi * self.rayon**2
