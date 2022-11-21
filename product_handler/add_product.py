from menu import products


def add_product(products, new_product):
    add_item = dict(zip(products, new_product))
    print(add_item)