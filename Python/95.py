class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def start(self):
        print("Car engine is starting")


car1 = Car()
car1.start()