# By using normal function we add items.
def add(a, b, c):
    return a+b+c


print(add(3, 4, 5))

# Same output can be obtained by using lambda function.
print((lambda a, b, c: a+b+c)(4, 5, 6))


# Uses of lambda functions.
list1 = list(range(21))  # Creating a list.
# Here we are creating lambda function.
sums = (lambda lis: sum(x**2 for x in lis))
# Here we are calling the lambda function by passing our list.
result = sums(list1)
print(result)

# We can also pass list in this way.
result = (lambda lis: sum(x**2 for x in lis))(list1)
print(result)

# We can be done more simplly.
print((lambda lis: sum(x**2 for x in lis))(list1))

# There is an other way to do so , by using lambda and map function.
sum_of_squares = sum(map(lambda x: x**2, list1))
print("Sum of squares:", sum_of_squares)
