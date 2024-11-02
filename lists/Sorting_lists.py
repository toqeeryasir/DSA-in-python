# Defined a list.
numbers = [10, 6, 9, 4, 8, 2, 7, 5, 3, 1]
# To sort our original list in assending order.
numbers.sort()
print(numbers)

# We can also sort list in desending order.
numbers.sort(reverse=True)
print(numbers)

# This will creat anew sorted list, and original list will remain the same.
new_list = sorted(numbers)
new_list = sorted(numbers, reverse=True)  # new reversed sorted list.
print(new_list)
print(numbers)  # We can see that original list is same as it is.

# If we have a list of tuples and we wanna sort it according to their prices.
items = [
    ("dettol", 200),
    ("shampoo", 244),
    ("biscuits", 150),
    ("coffee", 199),
    ("cake", 311)
]
# We need to creat a function that returns value of each item from the list.


def items_sort(items):
    return items[1]


# And here we need to pass reference of this function to the sort function.
items.sort(key=items_sort)
print(items)  # Sorted list according to prices.

# But there is a batter and simple way to do so, with lambda function.
items.sort(key=lambda item: item[1])
print(items)

# We can also sort it in reverse order.
items.sort(key=lambda item: item[1], reverse=True)
print(items)  # Sorted list in reversed order.
