#shopping = ["Milk", "Bread", "Eggs", "Apples"]
#for item in shopping:
 #   print(item)

#PROJECT- SHOPPING LIST PROGRAM

shopping=[]
a=input("Enter item: ")
b=input("Enter item: ")
c=input("Enter item: ")


shopping.append(a)
shopping.append(b)
shopping.append(c)

answer=input("Do you want to add another item(yes or no)")
while(answer=="yes"):
    item=input("Enter item: ")
    shopping.append(item)

    answer = input("Do you want to add another item? (yes/no): ")
print("\nShopping List: ")

for item in shopping:
    print(item)

print("Total items:", len(shopping))

#remove an item
answer = input("\nDo you want to remove an item? (yes/no): ")

if answer == "yes":
    item = input("Which item do you want to remove? ")

    if item in shopping:
        shopping.remove(item)
        print("Item removed.")
    else:
        print("Item not found.")

# Show updated list
print("\nUpdated Shopping List:")
for item in shopping:
    print(item)

print("Total items:", len(shopping))