from square import Square
import pytest


@pytest.mark.parametrize('side, perimeter, area',
                         [
                             (4, 16, 16),
                             (10, 40, 100),
                             (7, 28, 49),
                         ])
def test_square(side, perimeter, area):
    r = Square(side)
    assert r.name == 'Square'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('side, perimeter, area',
                         [
                             (-4, 16, 16),
                             (0, 16, 40),
                             (7, 28, 49)
                         ])
def test_square_negative(side, perimeter, area):
    with pytest.raises(ValueError):
        Square(side)