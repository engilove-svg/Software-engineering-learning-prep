class LearningSession:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Hello, {self.name}!")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Goodbye, {self.name}!")


with LearningSession("Loveleen"):
    print("Learning Python is fun!")