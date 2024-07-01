import math


def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap without a temporary variable (basically expandin a tuple without parentheses).
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


array = []
siz = int(input("How many values u wanna input?\n"))
for index in range(siz):
    element = int(input(f"Input element no. {index+1}\n"))
    array.append(element)

print("Array before sorting:")
print(", ".join(map(str, array)))

bubble_sort(array)  # Calling the function.

print("Sorted array:")
print(", ".join(map(str, array)))
