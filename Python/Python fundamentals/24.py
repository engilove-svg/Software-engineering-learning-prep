#Largest of 3 Numbers
a, b, c = map(int, input("Enter three numbers: ").split())
if(a>=b and a>=c):
    print(f"{a} is Largest")
elif(b>=a and b>=c):
    print(f"{b} is largest")
else:
    print(f"{c} is largest.")