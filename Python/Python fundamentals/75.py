def calculate_price(price, tax=13):
    tax_amount  = price * tax / 100
    finalprice = price + tax_amount 
    return finalprice


print(calculate_price(100))
print(calculate_price(100, 5))