from figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0 or side_a >= side_b + side_c or side_b >= side_c + side_a or side_c >= side_a + side_b:
            raise ValueError(f'Can not create Triangle')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = 'Triangle'

    def get_area(self):
        p = self.get_perimeter() / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
