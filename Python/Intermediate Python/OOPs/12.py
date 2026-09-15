from dataclasses import dataclass


@dataclass
class Expense:
    description: str
    amount: float
    category: str


def calculate_total(expenses: list[Expense]) -> float:
    total = 0.0

    for expense in expenses:
        total += expense.amount

    return total


expenses = [
    Expense("Lunch", 15.50, "Food"),
    Expense("Coffee", 5.00, "Food"),
    Expense("Bus", 3.50, "Transport")
]

total = calculate_total(expenses)

print(total)