#even/odd
def even_number(n):
    return n % 2 == 0
    
n=int(input("Enter a number: "))

if even_number(n):
    print(f"{n} is Even")
else:
    print(f"{n} is Odd")