#sum of even numbers
n=int(input("Enter n: "))
total=0
for i in range(0,n+1,2):
    total=total+i
print(total)