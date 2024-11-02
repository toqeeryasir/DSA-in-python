def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


arr = []
length = int(input("How many values u wanna input?\n"))
for index in range(length):
    element = int(input(f"Input element no. {index+1}\n"))
    arr.append(element)

target = int(input("Element u wanna find!\n"))
result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
