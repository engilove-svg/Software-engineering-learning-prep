def calculate_discount(price, discount):
    discount_amount = price * discount / 100
    return price - discount_amount

result = calculate_discount(100, 20)
print(result)