
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(characters)

# We can access indivisual item of the list by passing its index.
print(characters[1])

# We can also pass negative index.
print(characters[-1])

# We can also modify items in the list.
characters[2] = 'L'
print(characters)

# List can also be converted into slices by using semicolon (:).
new_list = characters[0:3]
# Item at 3rd index will not be included.(originol list will remain the same.)
print(new_list)

# List can also be reversed by using double collon and negative one (::-1).
numbers = list(range(1, 21))
reversed_list = numbers[::-1]
print(reversed_list)

# Creating a list using range function.(by built in list function.)
list_of_numbers = list(range(1, 21))
print(list_of_numbers)

# We can also combine lists to creat one.
combined = characters + list_of_numbers
print(combined)

# String can also be a list.
string = list("I love pakistan")
# Spaces are also part of the list.(we have 15 items in the list).
print(string)
