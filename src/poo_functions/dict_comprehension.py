names = [
    ("name", "Alfredo"),
    ("lastname", "Morais"),
]


def convert_list_of_tuple_in_dict(obj: list):
    return {key: value for key, value in names}
