from menu import products

def get_product_by_id(id: dict):
    try:
        for i in range(0, len(products)):
            product = products[i] 
        if id == product["_id"]: 
            print(product)
    except TypeError as error:
        print('Identificador não encontrado')
        print(error)
        
   


