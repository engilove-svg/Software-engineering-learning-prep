while True:
    try:
        age = int(input("Enter your age: "))

        if age < 0 or age==0:
            print("Age cannot be zero or negative.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")

print("Your age is:", age)