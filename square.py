from figure import Figure


class Square(Figure):
    def __init__(self, side):
        if side <= 0:
            raise ValueError(f'Can not create Square')
        self.side = side
        self.name = 'Square'

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return 4 * self.side
