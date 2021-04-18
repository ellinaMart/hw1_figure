import pytest

from source.figure import Triangle, Rectangle, Square, Circle

triangle = Triangle(a=3, b=4, c=5, height=4)
square = Square(a=4)
rectangle = Rectangle(a=3, b=4)
circle = Circle(r=4)
figures = [triangle, rectangle, square, circle]

def test_area():
    assert triangle.get_area() == 6
    assert square.get_area() == 16
    assert rectangle.get_area() == 12
    assert round(circle.get_area(),2) == 50.27

def test_perimeter():
    assert triangle.get_perimeter() == 12
    assert square.get_perimeter() == 16
    assert rectangle.get_perimeter() == 14
    assert round(circle.get_perimeter(),2) == 25.13

def test_add_area_negative():
    with pytest.raises(ValueError):
        for figure in figures:
            figure.add_area(figure)

def test_add_area_positive():
    for figure in figures:
        if figure != triangle:
            assert figure.add_area(triangle) == figure.get_area() + triangle.get_area()
        elif figure != rectangle:
            assert figure.add_area(rectangle) == figure.get_area() + rectangle.get_area()
        elif figure != square:
            assert figure.add_area(square) == figure.get_area() + square.get_area()
        elif figure != circle:
            assert figure.add_area(circle) == figure.get_area() + circle.get_area()

