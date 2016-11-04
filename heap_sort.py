
def max_heap(array, root, end):

    while True:
        child = root*2+1
        if child > end: break
        if child+1 <= end and array[child] < array[child+1]:
            #pick the max child
            child = child+1
        if array[root] < array[child]:
            array[root], array[child] = array[child], array[root]
        # set child as root
            root = child
        else:
            break

def heap_sort(array):
    # build max_heap first
    n = len(array)
    first = int(n/2 -1)

    for start in range(first, -1, -1):
        max_heap(array, start, n-1)

    # get sort array by exchange the last element with the first element,
    # and then build heap again.
    for end in range(n-1, 0, -1):
        array[end], array[0] = array[0], array[end]
        max_heap(array, 0, end-1)
    return array
