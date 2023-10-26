import random
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


def timestamp() -> str:
    return f'{random.randint(2018, 2023)}-{random.randint(10,12)}-{random.randint(10, 28)}T16:16:15.827Z'


def status() -> str:
    return random.choice(['cancelled', 'placed', 'postponed'])


def heads_or_tail() -> bool:
    return random.choice([True, False])