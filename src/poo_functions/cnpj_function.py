"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""


def clean_cnpj(cnpj: str):
    new_cnpj = ""

    for letter in cnpj:
        try:
            int(letter)
            str(letter)
            new_cnpj = new_cnpj + letter
        except ValueError:
            continue

    return new_cnpj


def reduce_cnpj(cleaned_cnpj: str):
    if len(cleaned_cnpj) == 14:
        return cleaned_cnpj[:-2]
    return "CNPJ Inválido"


def convert_cnpj_to_list(reduce_cnpj: str):
    cnpj_list = []

    for number in reduce_cnpj:
        cnpj_list.append(int(number))

    return cnpj_list


def return_first_validator():
    return [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def return_second_validator():
    return [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def find_first_result_list(cnpj_list: list):
    first_validator = return_first_validator()

    first_result = []

    if len(cnpj_list) == len(first_validator):
        for first, second in zip(cnpj_list, first_validator):
            result = first * second
            first_result.append(result)
        return first_result
    else:
        return "Erro de validação de listas."


def standard_formula(result_list: list):
    total = sum(result_list)

    result = 11 - (total % 11)

    if result > 9:
        return 0
    return result


def find_second_result_list(cnpj_list: list):
    second_validator = return_second_validator()

    second_result = []

    if len(cnpj_list) == len(second_validator):
        for first, second in zip(cnpj_list, second_validator):
            result = first * second
            second_result.append(result)
        return second_result
    else:
        return "Erro de validação de listas."


def final_validator(cnpj: str, cnpj_list: list):
    changed_cnpj = list(clean_cnpj(cnpj))

    if cnpj_list == changed_cnpj:
        return True
    return False


cnpj = "04.252.011/0001-10"
changed_cnpj = clean_cnpj(cnpj=cnpj)
cleaned_cnpj = reduce_cnpj(cleaned_cnpj=changed_cnpj)
cnpj_list = convert_cnpj_to_list(reduce_cnpj=cleaned_cnpj)
third_list = find_first_result_list(cnpj_list=cnpj_list)
first_number = standard_formula(result_list=third_list)
cnpj_list_first = cnpj_list.append(first_number)
fourth_list = find_second_result_list(cnpj_list=cnpj_list)
second_number = standard_formula(result_list=fourth_list)
cnpj_list_second = cnpj_list_first.append(second_number)
final = final_validator(cnpj=cnpj, cnpj_list=cnpj_list_second)
print(final)
