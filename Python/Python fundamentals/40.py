#Count digits
n=int(input("Enter a number: "))
i=0
count=0
while(n>0):
    n=n//10#last digit
    count+=1
print(count)



