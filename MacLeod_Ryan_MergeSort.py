def mergeSort(arr):
    # if theres only 1 element in the list, then return
    if len(arr) <= 1:
        return arr

    # split the array if theres more than one element left
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    # return the sorted array
    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    # sort the elements in the list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # combine the 2 arrays together
    result.extend(left[i:])
    result.extend(right[j:])

    return result