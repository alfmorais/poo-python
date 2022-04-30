list_one = list(range(10))


def simple_list_comprehension(obj: list):
    list_comprehension = [number for number in obj]
    return list_comprehension


# example one
def to_resolve_squar_number(obj: list):
    lc_version_one = [number ** 2 for number in obj]
    return lc_version_one


# example two
def coordinates_with_list_comprehension(obj: list):
    return [(number, coordinate) for number in obj for coordinate in range(3)]


# lc_version_two = coordinates_with_list_comprehension(obj=list_one)
# print(lc_version_two)

# example three
names = ['alfredo', 'morais', 'neto']


def replace_zero_for_letter_o(obj: list):
    lc_version_three = [name.replace('o', '0') for name in obj]
    return lc_version_three


# example four
tuple_example = (
    ('Alfredo', 'name'),
    ('Morais', 'sobrenome'),
)


def convert_tuple_to_dict(obj: tuple):
    lc_version_four = [(key, value) for value, key in obj]
    dict_name = dict(lc_version_four)
    return dict_name


# example five
list_number = list(range(100))


def filter_number_divided_for_two(obj: list):
    return [value for value in obj if value % 2 == 0]


# example six
def filter_with_else(obj: list):
    return [value if value % 3 == 0 else 'is not' for value in obj]


# challenger
string = '0123456789' * 5
list_of_string = [
    '0123456789',
    '0123456789',
    '0123456789',
    '0123456789',
    '0123456789',
]
returned_value = '0123456789.0123456789.0123456789.0123456789.0123456789'


def challenger_with_list_comprehension(obj: str):
    slice_value = 10
    list_value = [
        obj[i : i + slice_value] for i in range(0, len(obj), slice_value)
    ]
    return '.'.join(list_value)
