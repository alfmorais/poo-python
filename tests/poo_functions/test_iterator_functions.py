from src.poo_functions.iterator_functions import (
    calculate_total_of_ecommerce,
    function_create_generator,
    get_next,
)


def test_calculate_total_of_ecommerce():
    products = [
        ("Computer", 150.0),
        ("Notebook", 587.0),
        ("Iphone 7", 254.0),
    ]

    expected_result = sum([150.0, 587.0, 254.0])
    result = calculate_total_of_ecommerce(obj=products)

    assert result == expected_result


def test_get_next():
    result = get_next()
    expected_result = list(range(10))

    assert result == expected_result


def test_function_create_generator():
    result = list(function_create_generator(number=10))
    expected_result = list(range(11))

    assert result == expected_result
