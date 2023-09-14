from figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError(f'Can not create Circle')
        self.radius = radius
        self.name = 'Circle'

    def get_area(self):
        return 2 * pi * self.radius

    def get_perimeter(self):
        return pi * self.radius ** 2
