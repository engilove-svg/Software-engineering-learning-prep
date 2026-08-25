#Grade calculator
name = input("Enter Student name: ")
math = int(input("Enter Math marks: "))
python = int(input("Enter Python marks: "))
sql = int(input("Enter SQL marks: "))
english = int(input("Enter English marks: "))
computerscience = int(input("Enter Computer Science marks: "))

if math < 0 or math > 100:
    print("Invalid Math marks.")
elif python < 0 or python > 100:
    print("Invalid Python marks.")
elif sql < 0 or sql > 100:
    print("Invalid SQL marks.")
elif english < 0 or english > 100:
    print("Invalid English marks.")
elif computerscience < 0 or computerscience > 100:
    print("Invalid Computer Science marks.")
else:
    total = math + python + sql + english + computerscience
    percentage = total / 5
    print(f"Student: {name}")
    print(f"Total: {total}")
    print(f"Percentage: {percentage}")

    if percentage>=90:
      print("Grade: A+")
    elif percentage>=80:
      print("Grade: A")
    elif percentage>=70:
      print("Grade: B")
    elif percentage>=60:
      print("Grade: C")
    elif percentage>=50: 
      print("Grade: D")  
    else:
      print("Grade: F")