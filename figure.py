from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

