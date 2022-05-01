from itertools import count


def programming_count(start: int, step: int, stop: int):
    counter = count(start=start, step=step)
    result = []

    for number in counter:
        result.append(number)

        if number >= stop:
            break

    return result
