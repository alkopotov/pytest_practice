import json
import csv

with open('../data/books.csv', 'r', newline='') as books_file:
    reader = csv.reader(books_file)
    header = next(reader)
    books_array = [dict(zip(header, row)) for row in reader]

books_array = [{'title': elem['Title'],
                'author': elem['Author'],
                'pages': elem['Pages'],
                'genre': elem['Genre']}
               for elem in books_array]

with open('../data/users.json', 'r') as users_file:
    users_array = json.loads(users_file.read())

users_array = [{'name': elem['name'],
                'gender': elem['gender'],
                'address': elem['address'],
                'age': elem['age'],
                'books': books_array[users_array.index(elem)::len(users_array)]
                } for elem in users_array]

with open('users_books.json', 'w') as result_file:
    result_file.write(json.dumps(users_array, indent=4))
