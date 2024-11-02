# Sets can store data of unique items.
# We define a set by using curly_braces.
first_set = {1, 2, 3, 4, 5}

# We can convert a list into a set.
list_1 = [2, 1, 6, 7, 8, 9, 10]
second_set = set(list_1)
print(type(second_set))

# If we have a list with repeated items we can convert it into unique items list by converting it into a set.
un_unique_list = [1, 1, 2, 3, 2, 4, 1]
unique_items = set(un_unique_list)
print(unique_items)  # But here we are getting a set insted of a list.
print(type(unique_items))
# We can convert this tuple of unique items into a list of unique items.
unique_items_list = list(unique_items)
print(unique_items_list)
print(type(unique_items_list))  # Here we get a list of unique items.

# Same as lists we can add new items to sets.
first_set.add(9)
print(first_set)

# And we can remove items from it.
first_set.remove(3)
print(first_set)

# And we can also remove item from the last index.
first_set.pop()
print(first_set)


# And can't get item from set because items in sets are unordered, (without sequence)


# We can take union , intersection and difference of two or more sets.
print(first_set | second_set)
print(first_set & second_set)
print(first_set - second_set)

# We can also check the presence of an item in our set.
if 6 in second_set:
    print("true")
