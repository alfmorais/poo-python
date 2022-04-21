import math
from datetime import datetime


def to_compute(ends, begin=1):
    position = begin
    factor = 1000 * 1000

    while position < ends:
        position += 1
        math.sqrt((position - factor) * (position - factor))


def main():
    starts_at = datetime.now()

    to_compute(ends=50_000_000)

    time = datetime.now() - starts_at
    return f'Finished in {time.total_seconds():.2f} seconds.'


if __name__ == '__main__':
    main()

# Finished in 19.50023300 seconds. -> 21/04/2022
