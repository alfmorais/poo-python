def hello(phrase, name):
    """This function will return the salution phase.

    Args:
        phrase (str): salution phase
        name (str): person name
    """
    return f'{name}, {phrase}'


def total_sum(number1, number2, number3):
    """This function will return total sum.

    Args:
        number1 (int/float): number
        number2 (int/float): number
        number3 (int/float): number
    """
    return number1 + number2 + number3


def porcentage(number, porc):
    """This function will return the porcentage plus the value.

    Args:
        number (int/float): value
        porcentage (int/float): porcentage quantity
    """
    return number + (number * (porc / 100))


def fizz_buzz_function(number):
    """_summary_

    Args:
        number (_type_): _description_
    """
    if number % 3 == 0:
        if number % 5 == 0:
            return 'FizzBuzz'
        return 'fizz'
    if number % 5 == 0:
        return 'buzz'
    return number
