from array import array

# Here 'i' is the type of data we wanna store in array and in list we are addind data to our array.
first_array = array("i", [1, 2, 3, 4, 5])
print(first_array)

# Same as lists we can add element.
first_array.append(6)
print(first_array)

# We can remove element from last of the array.
first_array.pop()

# We can remove element from specific index.
first_array.pop(3)
print(first_array)

# By using remove methode we can remove element without passing its index , just by adding its value.
first_array.remove(2)
print(first_array)

# We can get element by using index.
third_element = first_array[0]
print(third_element)

# We can overright or change an element at specific index.
first_array[0] = 44
print(first_array)
