# We use @dataclass because it automatically generates boilerplate methods such as __init__(), making classes that mainly store data shorter and cleaner.
from dataclasses import dataclass

@dataclass
class Expense:
    description : str
    amount: float
    category : str




class ExpenseTracker:
    def __init__(self):
        self.expenses : list[Expense]=[]

    def add_expense(self,expense):
        self.expenses.append(expense)

    def show_expenses(self) -> None:
        for expense in self.expenses:
          print(
             f"{expense.description} - "
             f"${expense.amount:.2f} - "
             f"{expense.category}"
            )

    def calculate_total(self):
        total=0
        for expense in self.expenses:
            total+=expense.amount

        return total

    def find_expense(self,description):
        for expense in self.expenses:
            if(expense.description == description):
                return expense
            
        return None
# Create expenses
expense1 = Expense("Lunch", 15.50, "Food")
expense2 = Expense("Bus", 3.50, "Transport")
expense3 = Expense("Coffee", 5.00, "Food")

# Create tracker
tracker = ExpenseTracker()

# Add expenses
tracker.add_expense(expense1)
tracker.add_expense(expense2)
tracker.add_expense(expense3)

# Display
print("Expenses:")
tracker.show_expenses()

# Total
print(f"\nTotal: ${tracker.calculate_total():.2f}")

# Search
result = tracker.find_expense("Lunch")
print(f"\nFound: {result}")