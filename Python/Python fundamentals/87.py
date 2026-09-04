try:
    x = int(input("Enter: "))
except ValueError:
    print("A")
else:
    print("B")
finally:
    print("C")
    