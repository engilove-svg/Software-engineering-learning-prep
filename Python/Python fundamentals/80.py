def print_student(**details):
    for number in details:
        print(number,":",details[number])


print_student(
    name="Loveleen",
    age=23,
    course="CSE"
)