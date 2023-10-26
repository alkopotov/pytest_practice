from random import choice, randint
from faker import Faker


def random_number(start: int = 11, end: int = 200) -> int:
    return randint(start, end)


def user_name() -> str:
    return Faker().user_name()


def first_name() -> str:
    return Faker().first_name()


def last_name() -> str:
    return Faker().last_name()


def email() -> str:
    return Faker().email()


def password() -> str:
    return Faker().password()


def phone() -> str:
    return Faker().phone_number()