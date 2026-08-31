def find_largest(numbers):
    largest=numbers[0]
    for number in numbers:

        if(number>largest):
           largest=number
    
    return largest

numbers = [3, 8, 4, 2, 7, 5, 1]
result = find_largest(numbers)

print(result)