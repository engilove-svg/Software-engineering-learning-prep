# Generators
def even_numbers(n):
    for number in range(0, n + 1, 2):
        yield number


for number in even_numbers(10):
    print(number)