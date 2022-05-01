from src.poo_functions.data import numbers, persons, products
from src.poo_functions.map_functions import (
    get_name,
    get_price,
    increase_value,
    multiplied_list_values
)


def test_get_name():
    result = get_name(obj=persons)
    expected_result = list(map(lambda person: person['name'], persons))

    assert result == expected_result


def test_get_price():
    result = get_price(obj=products)
    expected_result = list(map(lambda price: price['price'], products))

    assert result == expected_result


def test_increase_value():
    result = list(map(increase_value, products))
    expected_result = [
        {'name': 'Computer', 'price': 1650},
        {'name': 'Notebook', 'price': 3850},
        {'name': 'Keyboard', 'price': 165},
        {'name': 'Chair', 'price': 935},
        {'name': 'Desktop Table', 'price': 385},
        {'name': 'Mouse', 'price': 11},
        {'name': 'Head Phone', 'price': 169},
        {'name': 'Cellphone', 'price': 1320},
        {'name': 'Hard Disk', 'price': 174},
        {'name': 'Motherboard', 'price': 504},
    ]

    assert result == expected_result


def test_multiplied_list_values():
    result = multiplied_list_values(obj=numbers)
    expected_result = list(range(0, 21, 2))

    assert result == expected_result
