l1 = [1, 2, 3, 6, 7, 8, 45]
l2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

i = 0
j = 0

sorted_ll = []

while i < len(l1) and j < len(l2):

    if l1[i] < l2[j]:
        sorted_ll.append(l1[i])
        i += 1
    elif l1[i] > l2[j]:
        sorted_ll.append(l2[j])
        j += 1

if i < len(l1):
    sorted_ll.extend(l1[i:])
else:
    sorted_ll.extend(l2[j:])

print(sorted_ll)
