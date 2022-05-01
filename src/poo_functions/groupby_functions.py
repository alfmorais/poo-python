from itertools import groupby

students = [
    {'name': 'Alfredo', 'grade': 10},
    {'name': 'Joaquim', 'grade': 8.5},
    {'name': 'Denise', 'grade': 9.0},
    {'name': 'Joaquim Neto', 'grade': 10},
    {'name': 'Vilma', 'grade': 10},
    {'name': 'Viviane', 'grade': 8.5},
    {'name': 'Ricardo', 'grade': 9.0},
    {'name': 'Vera', 'grade': 10},
    {'name': 'Derek', 'grade': 8.5},
    {'name': 'Daiane', 'grade': 9.0},
    {'name': 'Renan', 'grade': 10},
    {'name': 'Bussola', 'grade': 8.5},
]


def ordenation(obj: dict):
    return obj.sort(key=lambda item: item['grade'])


def lambda_function():
    return lambda item: item['grade']


students_ordenated = ordenation(obj=students)
order = lambda_function()

students_groupby = groupby(students, lambda item: item['grade'])

for students_group, values in students_groupby:
    quantity = len(list(values))

    print(f'Nota: {students_group}')
    print(f'A quantidade alunos que tiraram essa nota: {quantity}')
    print()
