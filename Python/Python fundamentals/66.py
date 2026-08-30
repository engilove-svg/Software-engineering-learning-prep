# Looping through a dictionary
# loop through keys
student = {
    "name": "Loveleen",
    "age": 23,
    "course": "Computer Science"
}

for key in student:
    print(key)

# loop through values
for value in student.values():
    print(value)

#loop through both key and value
for key, value in student.items(): # It means:Give me the key and its corresponding value for every item in the dictionary.
    print(key, ":", value)

# checking a key 
if "name" in student:
    print("Name exists")