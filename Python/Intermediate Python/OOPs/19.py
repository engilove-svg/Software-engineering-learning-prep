def my_decorator(function):

    def wrapper():
        print("Starting function...")
        function()

    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()