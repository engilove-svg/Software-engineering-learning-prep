transactions = [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": 250},
    {"id": 3, "amount": 75},
    {"id": 4, "amount": 500},
    {"id": 5, "amount": 150},
]

# Create the generator 

def transaction_generator(transactions):
    for transaction in transactions:
        yield transaction

# use it 

for transaction in transaction_generator(transactions):
    print(transaction)

#Now let's say we only want transactions greater than or equal to $200.
print("let's say we only want transactions greater than or equal to $200.")
def large_transactions(transactions):
    for transaction in transactions:
        if transaction["amount"] >= 200:
            yield transaction

for transaction in large_transactions(transactions):
    print(transaction)