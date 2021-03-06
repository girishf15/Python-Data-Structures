#__author__ = girish


def binary_search(arr, start, end, x):

    if start <= end:

        mid = start + (end - start) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, mid + 1, end, x)
        else:
            return binary_search(arr, start, mid - 1, x)
    else:
        return -1


arr = [10, 20, 30, 40, 50, 60, 70, 80]

result = binary_search(arr, 0, len(arr) - 1, 50)

if result != -1:
    print("Element is present at index %s" % result)
else:
    print("Element is not present in array")
