import pytest

from src.poo_functions.list_comprehension import (
    challenger_with_list_comprehension, convert_tuple_to_dict,
    coordinates_with_list_comprehension, filter_number_divided_for_two,
    filter_with_else, replace_zero_for_letter_o, simple_list_comprehension,
    to_resolve_squar_number)


@pytest.fixture(scope='module')
def general_list():
    return list(range(10))


def test_simple_list_comprehension(general_list):
    expected_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    value = simple_list_comprehension(general_list)

    assert value == expected_value


def test_to_resolve_squar_number(general_list):
    expected_value = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    value = to_resolve_squar_number(general_list)

    assert value == expected_value


def test_coordinates_with_list_comprehension(general_list):
    expected_value = [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
        (3, 0),
        (3, 1),
        (3, 2),
        (4, 0),
        (4, 1),
        (4, 2),
        (5, 0),
        (5, 1),
        (5, 2),
        (6, 0),
        (6, 1),
        (6, 2),
        (7, 0),
        (7, 1),
        (7, 2),
        (8, 0),
        (8, 1),
        (8, 2),
        (9, 0),
        (9, 1),
        (9, 2),
    ]

    value = coordinates_with_list_comprehension(general_list)

    assert value == expected_value


def test_replace_zero_for_letter_o():
    names = ['alfredo', 'morais', 'neto']
    expected_result = ['alfred0', 'm0rais', 'net0']

    result = replace_zero_for_letter_o(names)

    assert result == expected_result


def test_convert_tuple_to_dict():
    obj = (
        ('Alfredo', 'name'),
        ('Morais', 'sobrenome'),
    )

    expected_result = {
        'name': 'Alfredo',
        'sobrenome': 'Morais',
    }

    result = convert_tuple_to_dict(obj)

    assert result == expected_result


def test_filter_number_divided_for_two(general_list):
    expected_result = [0, 2, 4, 6, 8]

    result = filter_number_divided_for_two(general_list)

    assert result == expected_result


def test_filter_with_else(general_list):
    expected_result = [
        0,
        'is not',
        'is not',
        3,
        'is not',
        'is not',
        6,
        'is not',
        'is not',
        9,
    ]

    result = filter_with_else(general_list)

    assert result == expected_result


def test_challenger_with_list_comprehension():
    example = '0123456789' * 5

    expected_result = '0123456789.0123456789.0123456789.0123456789.0123456789'

    result = challenger_with_list_comprehension(example)

    assert result == expected_result
