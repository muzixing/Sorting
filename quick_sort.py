def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([x for x in arr[1:] if x < pivot]) + [pivot] + qsort([x for x in arr[1:] if x >= pivot])


def quick_sort(array, left, right):
    if left >= right:return array
    lp = left
    rp = right
    mid = array[right]
    while lp < rp:
        while array[lp] <= mid and lp < rp:
            lp += 1
        while array[rp] >= mid and rp > lp:
            rp -= 1
        array[lp], array[rp] = array[rp], array[lp]
    array[lp], array[right] = array[right], array[lp]

    quick_sort(array, left, lp-1)
    quick_sort(array, lp+1, right)
    return array
