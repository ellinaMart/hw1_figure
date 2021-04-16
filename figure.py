import math

class Figure:
    def __init__(self, name, angles):
        self.name = name
        self.angles = angles
    def get_perimeter(self):
        pass
    def get_area(self):
        pass

class Triangle(Figure):
    def __init__(self, a, b, c, height):
        super().__init__('triangle', 3)
        self.a = a
        self.b = b
        self.c = c
        self.height = height

    def get_area(self):
        return 0.5 * self.a * self.height

    def get_perimeter(self):
        return self.a + self.b + self.c

class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__('rectangle', 4)
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def get_perimeter(self):
        return 2 * (self.a + self.b)

class Square(Figure):
    def __init__(self, a):
        super().__init__('square', 4)
        self.a = a

    def get_area(self):
        return self.a ** 2

    def get_perimeter(self):
        return self.a * 4

class Circle(Figure):
    def __init__(self, r):
        super().__init__('rectangle', 4)
        self.r = r

    def get_area(self):
        return math.pi * (self.r ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.r
