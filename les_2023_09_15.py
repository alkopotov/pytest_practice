def sum_elems(start: int, end: int):
    elems = [e for e in range((start, end)[start > end], (end, start)[start > end] + 1)]
    print(sum(elems))
    print(list(filter(lambda x: x % 2 == 0, elems)))


sum_elems(1, 10)
sum_elems(11, 2)
sum_elems(5, 5)


def adder(*args: int, **kwargs: int):
    print(sum(args) + sum(kwargs.values()))


adder(2, 5, 6, x=1, y=2)
adder(7, 10, 11, x=24, y=20, z=12)
