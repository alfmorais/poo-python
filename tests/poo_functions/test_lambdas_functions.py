from src.poo_functions.lambdas_functions import list_sorted, supermarket_list


def test_list_sorted_with_reverse_false():
    response = list_sorted(supermarket_list, position=0, reverse=False)

    expected_result = supermarket_list

    assert response == expected_result


def test_list_sorted_with_reverse_true():
    response = list_sorted(supermarket_list, position=0, reverse=True)

    expected_result = [
        ['product5', 55],
        ['product4', 35],
        ['product3', 45],
        ['product2', 25],
        ['product1', 99],
    ]

    assert response == expected_result


def test_list_sorted_with_position_one_reverse_false():
    response = list_sorted(supermarket_list, position=1, reverse=False)

    expected_result = [
        ['product2', 25],
        ['product4', 35],
        ['product3', 45],
        ['product5', 55],
        ['product1', 99],
    ]

    assert response == expected_result


def test_list_sorted_with_position_one_reverse_true():
    response = list_sorted(supermarket_list, position=1, reverse=True)

    expected_result = [
        ['product1', 99],
        ['product5', 55],
        ['product3', 45],
        ['product4', 35],
        ['product2', 25],
    ]

    assert response == expected_result
