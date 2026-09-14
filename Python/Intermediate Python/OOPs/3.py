class Expense:

    def __init__(self,name,amount,category):
        self.name=name
        self.amount=amount
        self.category=category

    def show_expense(self):
        print("Expense: ",self.name)
        print("Amount: ",self.amount)
        print("Category: ",self.category)

    def get_amount(self):
        return self.amount
    
expenses = []
name = input("Enter expense name: ")
amount = float(input("Enter amount: "))
category = input("Enter category: ")

expense1 = Expense("Groceries", 50, "Food")
expense2 = Expense("Gas", 40, "Transport")

expense = Expense(name, amount, category)

expenses.append(expense)

expense.show_expense()

expenses = [expense1, expense2]
total = 0

for expense in expenses:
    total += expense.get_amount()

print("Total:", total)