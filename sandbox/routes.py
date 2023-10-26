from enum import Enum


class APIRoutes(str, Enum):
    USER = '/user/'

    def __str__(self) -> str:
        return self.value
