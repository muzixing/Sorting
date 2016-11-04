
def select_sort(array):
    length = len(array)
    for i in range(length):
        min = i
        for j in range(i,length):
            if array[min] > array[j]:
                min = j
        array[i], array[min] = array[min], array[i]

    return array

if __name__ == "__main__":
    test = [2, 1, 3, 4, 2, 5, 7, 3, 6, 10, 5, 15, 24, 100, 23, 45, 76, 3, 12, 23, 123, 5432, 12, 2, 0, 234, 0, 122,
            3, 7, 8, 9, 238, 1000, 2345, 5678, 223, 567, 345, 11245, 3345, 345, 12, 345]
    print(select_sort(test))