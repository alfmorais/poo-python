import pytest
from src.poo_functions.list_comprehension import (
    simple_list_comprehension,
    to_resolve_squar_number,
    coordinates_with_list_comprehension,
    # replace_zero_for_letter_o,
    # convert_tuple_to_dict,
    # filter_number_divided_for_two,
    # filter_with_else,
    # challenger_with_list_comprehension,
)


@pytest.fixture(scope="module")
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
        (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2),
        (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2),
        (6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2),
        (8, 0), (8, 1), (8, 2), (9, 0), (9, 1), (9, 2)
    ]

    value = coordinates_with_list_comprehension(general_list)

    assert value == expected_value
