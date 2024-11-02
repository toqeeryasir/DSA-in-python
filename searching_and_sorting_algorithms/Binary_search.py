def binary_search(arr, target):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


arr = []
length = int(input("How many values u wanna input?\n"))
for index in range(length):
    element = int(input(f"Input element no. {index+1}\n"))
    arr.append(element)
arr.sort()
target = int(input("Element u wanna find!\n"))
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index-> {result}")
else:
    print("Element not found")
