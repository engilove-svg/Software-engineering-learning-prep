# finally runs whether an exception happens or not.

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("Valid number:", number)
finally:
    print("Program finished.")