# Defining a list.
items = [1, 2, 3, 4, 5]

# We can assign each indivisual item to different variablel.
first = items[0]
second = items[1]
third = items[2]
fourth = items[3]
print(first, second, third, fourth)

# There is an easy way to do so.
# There is an issue the number of variables on left side should be equal to the number of items in the list, other wise we will get an error.
first, second, third, fourth, fifth = items
print(first, second, third, fourth, fifth)

# If we want to get only first few items then we can do so in the following way.
# Here remaining variable is a new list, with remaining items from the items_list.
first, second, *remaining = items
print(first, second, "\n", *remaining)

# We can also assign last items from the list to a variable just by adding the variable after the unpacking list -> *remaining.
first, *remaining, second = items
print(first, second, "\n", *remaining)

# By using loop we can print all the items of the list.
for item in items:
    print(item)

# If we want to print the index of each item as well.
# Here enumerate keword gives an item as well as its index.
for index, item in enumerate(items):
    print(index, item)
