def student_info(**kwargs):
    for number in kwargs:
        print(number,kwargs[number])

student_info(name="Loveleen", age=23, course="CSE")

# *args collects positional arguments -->tuple
# **kwargs collects keyword arguments -->dictionary