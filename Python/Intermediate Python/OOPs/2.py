#constructor

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")
        print(f"I study {self.course}")

student1=Student("Loveleen",23,"CSE")
student2=Student("Priya",21,"ECE")

student1.introduce()
