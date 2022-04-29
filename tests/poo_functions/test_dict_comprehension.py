from src.poo_functions.dict_comprehension import convert_list_of_tuple_in_dict


def test_convert_list_of_tuple_in_dict():
    names = [
        ("name", "Alfredo"),
        ("lastname", "Morais"),
    ]

    expected_result = {
        "name": "Alfredo",
        "lastname": "Morais",
    }

    result = convert_list_of_tuple_in_dict(names)

    assert result == expected_result
