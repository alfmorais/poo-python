def multiplied_list_values(obj: list):
    return list(map(lambda x: x * 2, obj))


def get_price(obj: list):
    return list(map(lambda price: price['price'], obj))


def increase_value(obj: dict):
    obj['price'] = round(obj['price'] * 1.10)
    return dict(obj)


def get_name(obj: dict):
    return list(map(lambda person: person['name'], obj))
