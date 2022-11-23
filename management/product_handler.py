from menu import products


def get_product_by_id(id) -> None: 
    if type(id) != int:
        raise TypeError("product id must be an int")
    for product in products:
        for _id in product.values():
            if _id == id:
                return product
    return {}



def get_products_by_type(types):
    products_found = []
    if type(types) != str:
        raise TypeError("product type must be a str")
    for i in range(0, len(products)):
        product = products[i]
        if types == product["type"]:
            products_found.append(product)
        
    return products_found


def menu_report():
    tt_price = 0

    product_count = len(products)
    
    
    for product in products: 
        tt_price += product.get('price')
    average_price = round(tt_price / len(products), 1)


    types = []
    for i in range(0, len(products)):
        product = products[i]
        types.append(product["type"])
    
    new_type = []
    for type in types:
        qtd = types.count(type)
        new_type.append(qtd)
    # print(new_type)
    max_valor = max(*new_type) 
    index = new_type.index(max_valor)
    print(index)
    most_common_type = types[index]
    print(most_common_type)
       
        
        
    
  

    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"
    

def add_product(products, **new_product) -> None:
    next_id = 0
    if len(products) == 0:
        next_id = 1
    for product in products:
        if product["_id"] >= next_id:
            next_id = product["_id"] + 1  
    new_product["_id"] = next_id 
    products.append(new_product)
    return new_product