# Defining a dictionary by using curlybraces {}.
# In dects we pass a key and a value.
# Key is a raference to our value.
# Here  names are keys and roll numbers are values.
first_dict = {"toqeer": 206, "faizan": 207, "abdullah": 250}
print(first_dict)

# Just like lists we can also define dicts by using built_in function "dict".
built_in = dict(yasir=+923238107374, mom="zzzz-zzzz-zzz")
print(built_in)

# We can add an item to our dict.
first_dict["gulfam"] = 205
print(first_dict)

# We can remove an item.
del first_dict["faizan"]
print(first_dict)

# And we can update the value.
first_dict["gulfam"] = 204
print(first_dict)

# We can check the existence of an item.
if "abdullah" in first_dict:
    print("Yes")
# We can also use get methode to check the existence of an item or to access an item.
print(first_dict.get("gulfam"))
