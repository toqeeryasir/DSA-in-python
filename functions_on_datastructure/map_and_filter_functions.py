# Filter & Lambda functions.
lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# It itrates over all the items just like loop.
even_numbers = list(filter((lambda x: x % 2 == 0), lists))
print(even_numbers)


# Same output without using lambda function, by using list comprehensions.
even_numbers = [x for x in lists if x % 2 == 0]
print(even_numbers)

# Getting prices of each item in the list.
products = [
    ("shampoo", 100),
    ("biskits", 200),
    ("cake", 300)
]

prices = list(map(lambda item: item[1], products))
print(prices)

# By using of filter function separating items with low price than 200.
filtered = list(filter(lambda item: item[1] < 200, products))
print(filtered)

# If we wanna store only value of that products in the list.
filtered = list(map(lambda item: item[1], filter(
    lambda item: item[1] < 200, products)))
print(filtered)

# We can achieve the same result by using list comprehensions.
filtered = [item[1] for item in products if item[1] < 200]
print(filtered)
