
def shell_sort(array):
    length = len(array)
    gap = round(length/2)

    while gap>0:
        for i in range(gap, length):
            #tmp = array[i]
            #j = i
            #while (j>=gap and array[j-gap]>tmp):
                # switch
            #    array[j] = array[j-gap]
            #    j = j - gap
            #array[j] = tmp
            if array[i] < array[i-gap]:
                array[i], array[i-gap] = array[i-gap], array[i]
        gap = round(gap/2)

    return array

