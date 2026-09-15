class BankAccount:
    def __init__(self, balance):
        self._balance = balance

#The _balance convention means:

#"This attribute is intended for internal use; don't modify it directly unless you know what you're doing."

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Balance cannot be negative")
        else:
            self._balance = value

account = BankAccount(1000)

account.balance = 2000
print(account.balance)

account.balance = -500
print(account.balance)
    
#when you write account.balance python uses @property method
# right now we can read the balance , we need to use setter