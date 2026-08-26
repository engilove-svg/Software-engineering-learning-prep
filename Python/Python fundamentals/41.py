#reverse a number
n=int(input("Enter a number: "))
reverse=0
while(n>0):
    last_digit=n%10#get the last digit
    reverse = reverse * 10 + last_digit#build reverse
    n=n//10#removing the last digit
    
print(reverse)

