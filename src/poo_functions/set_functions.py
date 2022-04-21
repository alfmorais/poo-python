"""
# add, update, clear, discard
# union
# intersection - (all elements in both sets)
# difference - (elements in left side only)
# symmetric_difference - (elements in both sets but not in one set)

from random import randint


first_set = {1, 2, 3, 4, 5, 6, 7}
print(first_set)

# add function
second_set = set()
second_set.add(1)
second_set.add(2)
second_set.add(3)
second_set.add(4)
second_set.add(("1", "2", 3))
print(second_set)

# discard function
second_set.discard(4)
print(second_set)

# update function
# second_set.update(4, 5)
# print(second_set)

# remove elements duplicated in list
super_market_list = [1, 1, 1, 2, 2, 3, 3, 5, 5, 5, 4, 4]
print(type(super_market_list))
print(super_market_list)
super_market_set = set(super_market_list)
print(type(super_market_set))
print(super_market_set)
super_market_list = list(super_market_set)
print(type(super_market_list))
print(super_market_list)

# union
set_one = {1, 2, 3, 4, 5}
set_two = {1, 2, 3, 4, 5, 6}

set_three = set_one | set_two
print(
    f"First set: {set_one}\n",
    f"Second set: {set_two}\n",
    f"Union set: {set_three}\n",
)

# intersection
set_intersection = set_one & set_two
print(set_intersection)

# difference
set_one.add(7)
set_difference = set_one - set_two
print(set_difference)

# symmetric_difference
symmetric_difference = set_one - set_two
print(symmetric_difference)

# É uma lista de lista de números inteiros
# As listas internas tem o tamanho de 10 elementos
# As listas internas contém números entre 1 a 10 e eles podem ser duplicados

# Exercicio
# Cria uma função que encontra os dois primeiros números duplicados na lista interna:
# Requisitos:
# A ordem dos números duplicados é considerada a partir da
# segunda ocorrência(o número duplicado em si)
# se não encontrar duplicados na lista retorne -1
"""
from random import randint


def list_generator():
    """This function will generator a list of 10 list with 10 elements each one."""
    main_list = list()
    first_list = list()
    second_list = list()
    third_list = list()
    fourth_list = list()
    fifth_list = list()
    sixth_list = list()
    seventh_list = list()
    eighth_list = list()
    ninth_list = list()
    tenth_list = list()

    main_list.append(first_list)
    main_list.append(second_list)
    main_list.append(third_list)
    main_list.append(fourth_list)
    main_list.append(fifth_list)
    main_list.append(sixth_list)
    main_list.append(seventh_list)
    main_list.append(eighth_list)
    main_list.append(ninth_list)
    main_list.append(tenth_list)

    for list_element in main_list:
        for _ in range(10):
            number_generator = randint(0, 10)
            list_element.append(number_generator)
    return main_list


def check_duplicated_number(main_list: list):
    """This function will check the first element duplicated in the list of list"""
    checked_numbers = set()
    first_duplicated_number = -1

    for number in main_list:
        if number in checked_numbers:
            first_duplicated_number = number
            break

        checked_numbers.add(number)
    return first_duplicated_number
