
def insertion_sort(array):
    length = len(array)
    for i in range(1, length):
        for j in range(i,0,-1):
            if array[i]<array[j]:
                array[j], array[i] = array[i], array[j]
    return array

