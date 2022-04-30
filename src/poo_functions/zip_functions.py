# Zip - Union Interators
# Zip Longest - Itertools


def sum_list_with_zip_function(first_list: list, second_list: list):
    result = []
    for first_value, second_value in zip(first_list, second_list):
        number_result = first_value + second_value
        result.append(number_result)
    return result


# first_list = [1, 2, 3, 4, 5, 6, 7]
# second_list = [1, 2, 3, 4]

# result = sum_list_with_zip_function(first_list=first_list, second_list=second_list)
# print(result)
