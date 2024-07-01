# Defining a list.
numbers = [1, 2, 3, 4, 5]

# If we wanna find the index of an item in the list.
print(numbers.index(3))

# Adding items into the list.
numbers.append(44)  # Adding an item at the end of the list.
print(numbers)
numbers.insert(2, "python")  # Adding an item at specific index.
print(numbers)

# Remove items from the list.
numbers.pop()  # Removing an item from the end of the list.
print(numbers)
numbers.pop(4)  # We can remove itme from specific index.
print(numbers)

# By using remove methode we can remove item without knowing its index.
numbers.remove("python")
print(numbers)

# We can delete a single or a range of items by using delete methode.
del numbers[3]  # Deleting a single item.
print(numbers)
del numbers[1:]  # Deleting a range of items.
print(numbers)

# To delete all the items from the list.
numbers.clear()
print(numbers)
