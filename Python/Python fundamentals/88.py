# multiple exceptions

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print(result)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("You cannot divide by zero.")