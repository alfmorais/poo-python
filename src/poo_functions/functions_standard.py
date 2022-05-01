from random import randint


def random_numbers_for_lotofacil():
    numbers = set()

    while True:
        number = randint(0, 25)
        numbers.add(number)

        if len(numbers) >= 14:
            break

    return numbers


def generate_lotofacil_numbers(quantity: int):
    game = []

    for _ in range(quantity + 1):
        numbers = random_numbers_for_lotofacil()
        game.append(numbers)

    return game


games = generate_lotofacil_numbers(quantity=15)
print(games)
