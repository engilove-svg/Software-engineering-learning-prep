# DICTIONARIES
# A dictionary stores data as: key → value

student = {
    "name": "Loveleen",
    "age": 23,
    "course": "Computer Science",
    "country": "canada"
}
student["age"]=24
print(student["name"],student["age"],student["course"],student["country"])
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
print(student.get("phone", "Not available"))
# pop()
student.pop("country")

print(student)