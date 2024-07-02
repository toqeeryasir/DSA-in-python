# Tuples are same as lists but we can not modify them we can't add new items to it and can't remove or delete items from these.
# To define a tuple we use parentheses ().
first_tuple = (1, 2, 3, 4, 5)
# Tuple can also be defined without parentheses, but we need to add a comma ,.
first_tuple = 1, 2, 3, 4, 5

# A list can be changed in touple by using touple methode.
first_list = [1, 2, 3, 4, 5]
list_to_tuple = tuple(first_list)
print(type(list_to_tuple))

# We can unpack tuple.
a, b, c, d, e = first_tuple
print(a, b, c, d, e)

# We can get items of the tuple.
a = first_tuple[4]
print(a)

# To get more then one items we can use collon : .
multiple = first_tuple[1:3]
print(multiple)

# We can check is a specific item exists in our tuple.
if 5 in first_tuple:
    print("true")

# We can also add or merge tuples.
second_tuple = (6, 7, 8, 9, 10)
new_tuple = first_tuple + second_tuple
print(new_tuple)


# Due to this ability of tuple we can swap walues in a single line of code.
a = 22
b = 44

a, b = b, a # Basiclly here we are unpacking a tuple.
print('a: ', a)
print('b: ', b)