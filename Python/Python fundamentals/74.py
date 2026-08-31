def calculate_average(numbers):
    count=0
    total=0
    
    for number in numbers:
        total=total+number
        count=count+1

    average=total/count
    return average

numbers = [10, 20, 30, 40, 50]
result=calculate_average(numbers)
print(result)