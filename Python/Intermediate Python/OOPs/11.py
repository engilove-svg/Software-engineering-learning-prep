def calculate_expenses(expenses: list[float]) -> float:
    return sum(expenses)


expenses = [10.5, 20.0, 15.5]

total = calculate_expenses(expenses)

print(total)