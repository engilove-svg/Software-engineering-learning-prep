def count_positive(numbers):
    count=0
    for number in numbers:
        if number > 0:
            count=count+1

    return count

numbers = [3, 8, 4, 2, 7, 5, 1]
result = count_positive(numbers)
print(result)