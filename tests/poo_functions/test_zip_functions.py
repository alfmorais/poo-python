from src.poo_functions.zip_functions import sum_list_with_zip_function


def test_sum_list_with_zip_function():
    first_list = list(range(10))
    second_list = list(range(4))

    expected_result = [0, 2, 4, 6]
    result = sum_list_with_zip_function(first_list, second_list)

    assert result == expected_result
