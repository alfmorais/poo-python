from src.poo_functions.count_functions import programming_count


def test_programming_count():
    result = programming_count(start=10, step=2, stop=20)

    expected_result = [10, 12, 14, 16, 18, 20]

    assert result == expected_result
