# When we use single astres * or souble astres ** at the start of an itrable , we can unpack it.
# Lets say we wanna creat a list of integers by using the range function .
test_list = [*range(1, 21)]
print(test_list)  # Printing all the values in a brackets.

# Buy we can print these endivisually by using unpacking operator.
print(*test_list)

# Just like lists we can also use unpacking operator with dictionaries.
dictionary_1 = dict(ali=22, hamza=30, yasir=40)
print(*dictionary_1)  # This will only print keys.

# We can also combine dictionaries.
dictionary_2 = dict(tofiq = 11, hassan = 55, faizan = 77)
combined = {**dictionary_1, **dictionary_2}
print(combined)

# Or we can pass a string directly.
combined = {**dictionary_1, **dictionary_2, "x":206} 
print(combined)