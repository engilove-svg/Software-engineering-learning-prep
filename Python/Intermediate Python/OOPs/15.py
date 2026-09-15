#composition

from dataclasses import dataclass


@dataclass
class Expense:
    description: str
    amount: float
    category: str

    def display(self):
        print(f"{self.description} - ${self.amount:.2f} - {self.category}")


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def show_expenses(self):
        for expense in self.expenses:
            expense.display()


expense1 = Expense("Lunch", 15.50, "Food")
expense2 = Expense("Bus", 3.50, "Transport")

tracker = ExpenseTracker()

tracker.add_expense(expense1)
tracker.add_expense(expense2)

tracker.show_expenses()