from menu import products
from product_handler.add_product import add_product
from product_handler.get_product_by_id import get_product_by_id
from product_handler.get_products_by_type import get_products_by_type
from product_handler.menu_report import menu_report


if __name__ == "__main__":
    print(get_product_by_id(28))
    print()
    print(get_products_by_type("drink"))
    print()
    print(menu_report())
    print()
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }
    print(add_product(products, new_product))
# main.py
...

