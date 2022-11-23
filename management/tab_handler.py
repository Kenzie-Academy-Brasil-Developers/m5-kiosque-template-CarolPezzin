import locale

from menu import products

def calculate_tab(table):
    total = 0
    
    for mesa in table:
        for product in products:
            if mesa["_id"] == product["_id"]:
                total = round(total + product["price"] * mesa["amount"], 2)
                
                valor_formatado = (total)
                
              
    return {'subtotal': f'${valor_formatado}'}