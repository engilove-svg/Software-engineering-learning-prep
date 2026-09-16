def count_down(n):
    while n>=1:
        yield n
        n-=1

for number in count_down(5):
    print(number)
