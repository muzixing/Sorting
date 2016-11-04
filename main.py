from sort.bubble_sort import bubble_sort
from sort.heap_sort import heap_sort
from sort.insertion_sort import insertion_sort
from sort.merge_sort import merge_sort
from sort.quick_sort import qsort, quick_sort
from sort.select_sort import select_sort
from sort.shell_sort import shell_sort

if __name__ == "__main__":
    test = [2, 1, 3, 4, 2, 5, 7, 3, 6, 10, 5, 15, 24, 100, 23, 45, 76, 3, 12, 23, 123, 5432, 12, 2, 0, 234, 0, 122,
            3, 7, 8, 9, 238, 1000, 2345, 5678, 223, 567, 345, 11245, 3345, 345, 12, 345]

    #print("bubble", bubble_sort(test))
    #print("insert", insertion_sort(test))
    #print("select", select_sort(test))
    #print("shell", shell_sort(test))
    #print("merge", merge_sort(test))
    #print("quick", qsort(test))
    print("quick_sort", quick_sort(test, 0,len(test)-1))
    print("heap_sort", heap_sort(test))