
def bubble_sort(arr):

    swapped = True

    while swapped:

        swapped = False

        for i in range(len(arr) - 1):

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

    print(arr)
    return arr

arr = [5,7,2,47,11,10,2,3,4,5]

print("Sorted --- >" , bubble_sort(arr))