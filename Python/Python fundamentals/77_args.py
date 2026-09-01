# Normally, a function expects a fixed number of arguments:
# But what if you don't know how many arguments the user will provide?

# That's where *args comes in.

def calculate_sum(*args):
    total=0
    for number in args:
       total=total+number
    return total

print(calculate_sum(10, 20, 30, 40))#*args collects all positional arguments into a tuple