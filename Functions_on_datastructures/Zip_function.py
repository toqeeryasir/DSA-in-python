# Defining two lists.
list_1 = ['a', 'b', 'c', 'd', 'e']
list_2 = [1, 2, 3, 4, 5]
# If we wanna combine each item of the list with the corresponding index item fo another list then.
# We use built_in zip function.
new_list = list(zip(list_1, list_2))
new_list = list(zip(list_1, list_2))
print(new_list)
print(new_list)

# Or we can also pass a string directly.
list_3 = "pakista"
new_list = list(zip(list_1, list_2, list_3))
print(new_list)
