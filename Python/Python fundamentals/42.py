#palindrome
n=int(input("Enter a number: "))
original=n
another_number=0
while(n>0):
    last_digit=n%10#getting last digit
    another_number=another_number*10+last_digit#reverse
    n=n//10
print(another_number)
if(original==another_number):
    print("Palindrome")
else:
    print("Not palindrome")
