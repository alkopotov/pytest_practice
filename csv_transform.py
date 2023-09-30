import csv
from decimal import Decimal

with open('data/grades.csv', newline='') as f:
    reader = csv.reader(f)
    # header = next(reader)
    header = [e.strip('" ') for e in next(reader)]
    print(header)
    array = [dict(zip(header, row)) for row in reader]


def get_num(e):
    return Decimal(e.strip())


def get_grade(num):
    grades = {
        95: 'A+',
        90: 'A',
        85: 'A-',
        80: 'B+',
        75: 'B',
        70: 'B-',
        65: 'C+',
        60: 'C',
        55: 'C-',
        50: 'D+',
        45: 'D',
        40: 'D-',
        35: 'E+',
        30: 'E',
        25: 'E-',
        20: 'F+',
        15: 'F',
        0: 'F-'
    }
    grade_key = min([[e, abs(e - num)] for e in grades.keys() if e <= num], key=lambda x: x[1])[0]
    return grades[grade_key]


res = [{'Student': elem['First name'].strip('" ') + ' ' + elem['Last name'].strip('" '),
        'Average Test': str((get_num(elem['Test1']) + get_num(elem['Test2']) + get_num(
            elem['Test3']) + get_num(elem['Test4']) + get_num(elem['Final'])) / 5),
        'Grade': elem['Grade'].strip('" ')} for elem in array]




print(*res, sep='\n')

with open('data/results.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', )
    writer.writerow(['Student', 'Average Test', 'Grade'])
    for e in res:
        writer.writerow([e['Student'], e['Average Test'], e['Grade']])
