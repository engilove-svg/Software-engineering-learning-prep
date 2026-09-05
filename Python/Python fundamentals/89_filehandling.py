with open("expenses.txt", "w") as file:
    file.write("Food: $20\n")
    file.write("Transport: $10\n")
with open("expenses.txt", "a") as file:
    file.write("Coffee: $5\n")
with open("expenses.txt", "r") as file:
    content = file.read()
    print(content)

with open("expenses.txt", "r") as file:
    lines = file.readlines()

print(lines)
# readlines() returns a list, where each line is a separate string:


with open("expenses.txt", "r") as file:
    for line in file:
        print(line.strip())# #strip() removes extra newline


#read()       → entire content
#readline()   → one line
#readlines()  → list of lines
with open("expenses.txt", "r") as file:
    print(file.read())
    file.seek(0)# moves the cursor back to position 0, which is the beginning.
    print(file.read())