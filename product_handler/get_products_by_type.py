from menu import products

def get_products_by_type(str: list):
    for i in range(0, len(products)):
        product = products[i]
        if str == product["type"]:
            try:
                print(product)
            except TypeError as error:
                print('Produto não encontrado')
                print(error)
