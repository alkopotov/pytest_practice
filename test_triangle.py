from triangle import Triangle
import pytest
from math import sqrt


@pytest.mark.parametrize('side_a, side_b, side_c, perimeter, area',
                         [
                             (3, 4, 5, 12, 6),
                             (6, 8, 10, 24, 24),
                             (7, 8, 9, 24, 26.832815),
                         ])
def test_triangle(side_a, side_b, side_c, perimeter, area):
    r = Triangle(side_a, side_b, side_c)
    assert r.name == 'Triangle'
    assert round(r.get_area(), 4) == round(area, 4)
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a, side_b, side_c, perimeter, area',
                         [
                             (-3, 4, 5, 12, 6),
                             (-6, 8, 10, 24, 24),
                             (7, 8, 17, 17, 25),
                             (10, 8, 17, 17, 25)
                         ])
def test_triangle_negative(side_a, side_b, side_c, perimeter, area):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)
