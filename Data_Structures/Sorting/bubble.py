
def bubble_sort(arr):

    swapped = True

    while swapped:

        swapped = False

        for i in range(len(arr) - 1):

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

    # print(arr)
    return arr


arr = [5, 7, 2, 47, 11, 10, 2, 3, 4, 5]

#print("Sorted --- >", bubble_sort(arr))


def bubble_sort_2(arr):

    n = len(arr)
    counter = 0

    print(n)

    for i in range(n):

        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print('-- {} - Swap {} and {}'.format(arr, arr[j+1], arr[j]))
            else:w
                print('-- {} - No Swap'.format(arr))
            counter += 1
    print(counter)

    return arr


print("arr", bubble_sort_2(arr))
