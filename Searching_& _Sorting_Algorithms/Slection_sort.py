import math


def bubble_sort(arr):
    length = len(arr)
    for x in range(length - 1):
        smallest = x
        for index in range(x + 1, length):
            if array[smallest] > array[index]:
                smallest = index
         # Swaping elements by tuple unpacking.
        array[smallest], array[x] = array[x], array[smallest]


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
