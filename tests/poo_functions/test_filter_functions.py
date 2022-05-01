from src.poo_functions.filter_functions import filter_numbers, filter_price
from src.poo_functions.data import numbers, products


def test_filter_numbers():
    result = filter_numbers(obj=numbers)
    expected_result = [number for number in numbers if number > 5]

    assert result == expected_result


def test_filter_price():
    result = filter_price(obj=products)
    expected_result = dict(filter(lambda price: price["price"] > 1000, products))

    assert result == expected_result
