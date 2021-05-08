import pytest

from source.figure import Triangle, Rectangle, Square, Circle

@pytest.fixture()
def default_figures():
    figures = [Triangle(a=3, b=4, c=5, height=4), Square(a=4), Rectangle(a=3, b=4), Circle(r=4)]
    yield figures
    del figures
