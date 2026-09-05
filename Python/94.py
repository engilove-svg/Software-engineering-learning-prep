import csv

with open("expenses.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    total=0
    for row in reader:
        amount = int(row[1])
        total+=amount
        print(f"{row[0]}: ${amount}")
    print(f"Total: ${total}")