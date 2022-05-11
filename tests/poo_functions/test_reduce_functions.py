from src.poo_functions.data import numbers, products
from src.poo_functions.reduce_functions import (reduce_with_numbers,
                                                reduce_with_products)


def test_reduce_with_numbers():
    result = reduce_with_numbers(obj=numbers)
    expected_result = sum(list(range(11)))

    assert result == expected_result


def test_reduce_with_products():
    result = reduce_with_products(obj=products)

    expected_result = 0
    for product in products:
        expected_result = expected_result + product['price']

    assert result == expected_result
