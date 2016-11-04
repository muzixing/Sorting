import time


def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def bubble_sort_1(array):
    t = time.time()
    length = len(array)
    last = length-1
    for i in range(length):
        flag = 1
        for j in range(last):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                last = j
                flag = 0
        if flag:
            break
    diff = t- time.time()
    print(diff)
    return array

if __name__ == "__main__":
    test = [2,1,3,4,2,5,7,3,6,10,5,15,24,100,23,45,76,3,12,23,123,5432,12,2,0,234,0,122,3,7,8,9, 238,1000,2345,5678,223,567,345,11245,3345,345,12,345]
    print(bubble_sort(test))
    print(bubble_sort_1(test))
