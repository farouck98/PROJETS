from shape import Shape
from circle import Circle
from rectangle import Rectangle

def main():
    cercle = Circle(4.5)
    print(cercle.area())

    rec = Rectangle(3, 5)
    print(rec.area())


if __name__ == "__main__":
    main()
