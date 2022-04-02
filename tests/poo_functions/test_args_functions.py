from src.poo_functions.args_functions import function_one, function_two


def test_function_one():
    response = function_one()

    assert response == "Hello World"


def test_function_two():
    response = function_two(function_one)

    assert response == "Hello World"
