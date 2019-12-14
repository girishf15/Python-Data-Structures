#__autho__ : "girish"

def binary_search(arrr, start, end, x):

    while start <= end:

        mid = start + abs(start - end) // 2

        if arr[mid] == x:
            return mid

        elif (arr[mid] < x):
            start = mid + 1

        else:
            end = mid - 1

        print(mid, start, end)

    return - 1

arr = [10, 20, 30, 40, 50, 60, 70, 80]

result = binary_search(arr, 0, len(arr) - 1, 30)

if result != -1:
    print("Element is present at index %s" % result)
else:
    print("Element is not present in array")