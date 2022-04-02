from poo_functions.poo_functions import (
    hello,
    total_sum,
    porcentage,
    fizz_buzz_function
)


def test_hello():
    name = "Alfredo"
    phrase = "Hello World!"

    response = hello(name=name, phrase=phrase)

    assert response == f"{name}, {phrase}"


def test_total_sum():
    number1 = 10
    number2 = 10
    number3 = 10

    response = total_sum(number1=number1, number2=number2, number3=number3)

    assert response == 30


def test_porcentage():
    number = 100.00
    porc = 10

    response = porcentage(number=number, porc=porc)

    assert response == 110.00


def test_fizz_buzz_function_three():
    number = 3

    response = fizz_buzz_function(number=number)

    assert response == "fizz"


def test_fizz_buzz_function_five():
    number = 5

    response = fizz_buzz_function(number=number)

    assert response == "buzz"


def test_fizz_buzz_function_fifteen():
    number = 15

    response = fizz_buzz_function(number=number)

    assert response == "FizzBuzz"


def test_fizz_buzz_function_error():
    number = 17

    response = fizz_buzz_function(number=number)

    assert response == 17
