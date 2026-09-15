from dataclasses import dataclass


@dataclass
class Expense:
    description: str
    amount: float
    category: str


def get_food_expenses(expenses: list[Expense]) -> list[Expense]:
    food_expenses = []

    for expense in expenses:
        if expense.category == "Food":
            food_expenses.append(expense)

    return food_expenses


expenses = [
    Expense("Lunch", 15.50, "Food"),
    Expense("Bus", 3.50, "Transport"),
    Expense("Coffee", 5.00, "Food"),
    Expense("Movie", 20.00, "Entertainment")
]


food_expenses = get_food_expenses(expenses)

for expense in food_expenses:
    print(expense)