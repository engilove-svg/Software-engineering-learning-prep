expenses = [
    {
        "category": "Food",
        "amount": 20
    },
    {
        "category": "Rent",
        "amount": 500
    },
    {
        "category": "Coffee",
        "amount": 5
    }
]
import json

with open("expenses.json", "w") as file:
    json.dump(expenses, file, indent=4)

with open("expenses.json", "r") as file:
    expenses = json.load(file)