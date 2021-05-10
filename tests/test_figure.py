import pytest

def test_area(default_figures):
    assert default_figures[0].get_area() == 6
    assert default_figures[1].get_area() == 16
    assert default_figures[2].get_area() == 12
    assert round(default_figures[3].get_area(),2) == 50.27

def test_perimeter(default_figures):
    assert default_figures[0].get_perimeter() == 12
    assert default_figures[1].get_perimeter() == 16
    assert default_figures[2].get_perimeter() == 14
    assert round(default_figures[3].get_perimeter(),2) == 25.13

def test_add_area_negative(default_figures):
    #негативный тест на проверку не геом фигуры, или той же фигуры, для которой вызываем метод
    with pytest.raises(ValueError):
        for figure in default_figures:
            figure.add_area(figure)

def test_add_area_positive(default_figures):
    # позитивный тест, проверяющий метод add_area для каждой пары фигур
    for figure in default_figures:
        if figure != default_figures[0]:
            assert figure.add_area(default_figures[0]) == figure.get_area() + default_figures[0].get_area()
        elif figure != default_figures[1]:
            assert figure.add_area(default_figures[1]) == figure.get_area() + default_figures[1].get_area()
        elif figure != default_figures[2]:
            assert figure.add_area(default_figures[2]) == figure.get_area() + default_figures[2].get_area()
        elif figure != default_figures[3]:
            assert figure.add_area(default_figures[3]) == figure.get_area() + default_figures[3].get_area()
