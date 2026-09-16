numbers = (x for x in range(10) if x % 2 == 0)

for number in numbers:
    print(number)

#"Generators produce values one at a time instead of storing all the values in memory,
#  so they are useful when working with large amounts of data."