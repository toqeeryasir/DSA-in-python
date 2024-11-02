def add(num1, num2=6):
    # Here we are returning multiple values:(by using a comma (,)).
    return (num1, num2, num1 + num2)


result = add(6, 44)
print(result)


def subtract(num1: int, num2: int) -> tuple:  # Here we are specifing number type & returning a tuple.
    return (num1, num2, num1 - num2)


result = subtract(44, 6)
print(result)


def multiply(*tuple):  # If we want to pass arbitrary number of arguments :
    total = 1
    for number in tuple:
        total *= number
    return total


# Here inside these () parenthesis we can pass 2, 3, ...  any amout of numbers.
result = multiply(3, 5, 6, 7, 9)
print(result)


# We can also pass keyword arguments by using ** two astress :
def data_of_person(**person):
    print(person["name"])
    print(person["id"])
    print(person["request"])


data_of_person(name="Toqeer", id=244, request="Pending")
