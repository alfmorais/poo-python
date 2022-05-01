def filter_numbers(obj: list):
    return list(filter(lambda x: x > 5, obj))


def filter_price(obj: dict):
    return dict(filter(lambda price: price["price"] > 1000, obj))
