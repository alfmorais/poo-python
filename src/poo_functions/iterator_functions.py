import sys
import time

example = list(range(10))


def function_convert_obj_in_iter(obj: list):
    object = iter(obj)
    result = []

    for _ in len(obj):
        result.append(next(object))

    return result


def return_quantity_bytes_in_list(obj: list):
    return sys.getsizeof(obj)


def create_generator():
    for number in range(10):
        yield number
        time.sleep(0.1)


def get_next():
    number = create_generator()

    result = []

    for item in number:
        result.append(item)

    return result


def function_create_generator(number: int):
    object = (x for x in range(number + 1))
    return object


def calculate_total_of_ecommerce(obj: list):
    return sum([float(y) for x, y in obj])
