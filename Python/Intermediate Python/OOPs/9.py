# dataclasses
from dataclasses import dataclass
@dataclass
class Expense:
    description : str
    amount : float
    category : str

    def display(self):
        print(f"{self.description} - ${self.amount:.2f} - {self.category}")
        

expense1 = Expense("Lunch", 15.50, "Food")
expense1.display()


