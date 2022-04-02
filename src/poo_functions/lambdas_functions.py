supermarket_list = [
    ['product1', 99],
    ['product2', 25],
    ['product3', 45],
    ['product4', 35],
    ['product5', 55],
]


def list_sorted(list, position, reverse=None):
    return sorted(list, key=lambda index: index[position], reverse=reverse)
