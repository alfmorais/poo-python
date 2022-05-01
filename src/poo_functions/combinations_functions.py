from itertools import combinations

"""
Combinations, Permutations e Product - Itertools
Combinations - Ordem não importa
Permutação - Ordem importa
Combinations e Permutação - ambos não repetem valores únicos
Produto - Ordem importa e repete valores unicos
"""

values_list = list(range(0, 500, 25))


def combinations_values(obj: list, value: int):
    return combinations(obj, value)


combinations_obj = combinations_values(values_list, 500)

for combinations_value in combinations_obj:
    print(combinations_value)
