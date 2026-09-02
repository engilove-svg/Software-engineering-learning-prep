def student_report(name, age=18, *scores, **details):
    print("Name: ",name)
    print("Age: ",age)
    print("Scores: ",scores)
    for number in details:
        print(number,":",details[number])
    

student_report(
    "Loveleen",
    23,
    80, 90, 85,
    course="CSE",
    city="Sault Ste. Marie"
)