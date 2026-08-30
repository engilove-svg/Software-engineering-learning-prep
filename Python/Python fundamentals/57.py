#Lists
shopping = ["Milk", "Bread", "Eggs", "Apples"]
print(shopping[0],shopping[2],shopping[-1])

#append()
#append() always adds one item at the end.

shopping.append("Mango")
print(shopping)

#insert()
#insert() lets you add an item at a specific position.

shopping.insert(1,"Butter")
print(shopping)

#extend()
#extend() adds multiple items to a list.
#append() can create a nested list.

shopping.extend(["Grapes","Strawberry"])
print(shopping)

#remove()
#remove() removes an item by its value.

shopping.remove("Strawberry")
print(shopping)

#pop()
#pop() removes an item using its index and also returns the removed item.

update=shopping.pop(2)
print(update)
print(shopping)

#clear()
#clear() removes everything from the list.

shopping.clear()
print(shopping)

#len()
#len() tells you how many items are in a list.

shopping = ["Milk", "Bread", "Eggs", "Apples"]
print(len(shopping))

#in
#check if an item exists

print("Milk" in shopping)
print("Chicken" in shopping)


#sort()
#sort() arranges the list in ascending order.

shopping.sort()
print(shopping)

numbers = [50, 10, 30, 20, 40]
numbers.sort()
numbers.reverse()#used to reverse
print(numbers)