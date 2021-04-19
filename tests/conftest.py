import pytest

from source.figure import Triangle, Rectangle, Square, Circle

@pytest.fixture()
def default_figures():
    triangle = Triangle(a=3, b=4, c=5, height=4)
    square = Square(a=4)
    rectangle = Rectangle(a=3, b=4)
    circle = Circle(r=4)
    figures = [triangle, square, rectangle, circle]
    yield figures
    del figures
