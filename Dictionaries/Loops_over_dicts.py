# Loops & comprehensions over dicts.
first_dict = {"toqeer": 206, "faizan": 207, "abdullah": 250}

for key in first_dict:
    print(key)
# To get value as well we can pass key as an index.
for key in first_dict:
    print(key, first_dict[key])

# Or we can do so by using item() methode.
for key in first_dict.items():
    print(key)  # Here we will get an key and item as a tuple.

# Here is a better wey to do so.
for key, value in first_dict.items():
    print(key, value)  # Now we get keys and values wothout tuple.

# We can also use comprehensions just like dictionaries.

list_test = [1, 2, 3, 4, 5]
# Applying comprehensions.
# Lets say we wanna add these numbers as squares to a new list.
new_list = [e * 2 for e in list_test]
print(new_list)

# Sanme thing can be done with dictionaries.
new_dict = {key: value * 2 for key, value in first_dict.items()}
print(new_dict)
