from functools import reduce


def reduce_with_numbers(obj: list):
    return reduce(lambda total, index: index + total, obj, 0)


def reduce_with_products(obj: dict):
    return reduce(lambda total, product: product['price'] + total, obj, 0)
