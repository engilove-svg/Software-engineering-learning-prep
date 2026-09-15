# composition
class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self):
        self.engine = Engine()#Main step of composition

    def start_car(self):
        self.engine.start()#Car is telling its contained Engine object to start.
        print("Car started.")

car=Car()
car.start_car()