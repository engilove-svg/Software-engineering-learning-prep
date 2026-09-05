#What is JSON?

# JSON = JavaScript Object Notation.
# JSON is mainly used to store and exchange structured data.
import json

expenses = {
    "Food": 20,
    "Rent": 500
}

with open("expenses.json", "w") as file:
    #json.dump(expenses, file)
    data=json.dumps(expenses)
    file.write(data)
# file.write() expects a string, but expenses is a dictionary.
