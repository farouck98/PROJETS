class Rectangle:
   def __init__(self, width:float, height:float):
       self.width = width
       self.height = height
   def area(self):
        return self.width * self.height
   def perimeter(self):
        return (self.width + self.height) * 2

r1 = Rectangle(5, 4)
print(r1.area(), r1.perimeter())
