lines = ["Food: $20\n", "Rent: $500\n", "Coffee: $5\n"]

with open("expenses.txt", "w") as file:
    for line in lines:
        data=line.strip()
        file.write(data + "\n")