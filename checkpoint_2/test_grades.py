import csv
from decimal import Decimal
import pytest

def get_num(e):
    return Decimal(e.strip())


def get_grade(num):
    grades = {
        90: 'A+',
        85: 'A',
        80: 'A-',
        75: 'B+',
        70: 'B',
        65: 'B-',
        60: 'C+',
        55: 'C',
        50: 'C-',
        45: 'D+',
        40: 'D',
        35: 'D-',
        30: 'E+',
        25: 'E',
        20: 'E-',
        0: 'F'
    }
    grade_key = min([[e, abs(e - num)] for e in grades.keys() if e <= num], key=lambda x: x[1])[0]
    return grades[grade_key]


with open('../data/grades.csv', newline='') as f:
    reader = csv.reader(f)
    # header = next(reader)
    header = [e.strip('" ') for e in next(reader)]
    print(header)
    array = [dict(zip(header, row)) for row in reader]

res = [{'Student': elem['First name'].strip('" ') + ' ' + elem['Last name'].strip('" '),
        'Average Test': str((get_num(elem['Test1']) + get_num(elem['Test2']) + get_num(
            elem['Test3']) + get_num(elem['Test4']) + get_num(elem['Final'])) / 5),
        'Grade': elem['Grade'].strip('" ')} for elem in array]

print(*res, sep='\n')

@pytest.mark.parametrize('item', res)
def test_grade(item):
    assert item['Grade'] == get_grade(Decimal(item['Average Test']))
