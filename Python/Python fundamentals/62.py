# sets: A set is a collection that stores unique values.
# The duplicates are automatically removed.

# sets don't use indexes like lists and tuples.

numbers = {10, 20, 10, 30, 20, 40, 10}
print(numbers)

# add()
numbers.add(50)
print(numbers)

# remove() vs discard()

# Difference is remove() cause an error and discard() does nothing if 100 is not there.
numbers.remove(30)
numbers.discard(20)
print(numbers)