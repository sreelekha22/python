def mergeSort(li):
    if len(li) > 1:
        mid = len(li) // 2
        left = li[:mid]
        right = li[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                li[k] = left[i]
                i += 1
            else:
                li[k] = right[j]
                j += 1
            k += 1

        # For all the remaining values
        while i < len(left):
            li[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            li[k] = right[j]
            j += 1
            k += 1


myList = [63, 26, 93, 17, 7, 31, 4, 50, 20]
print('Original list : ', myList)
mergeSort(myList)
print('Merge sorted  : ', myList)
