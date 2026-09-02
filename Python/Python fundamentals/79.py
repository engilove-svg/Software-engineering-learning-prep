def calculate_total(*prices):
    total=0
    for number in prices:
        total+= number
    return total


print(calculate_total(10, 20, 30))