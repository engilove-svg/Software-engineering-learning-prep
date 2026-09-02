def calculate_average(*scores):
    count=0
    total=0
    for number in scores:
        count=count+1
        total=total+number
    average=total/count
    return average

print(calculate_average(80, 90, 85))