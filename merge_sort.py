
def merge(l_list, r_list):
    l = 0
    r = 0
    result = []
    while (l < len(l_list) and r < len(r_list)):
        if l_list[l] > r_list[r]:
            result.append(r_list[r])
            r += 1
        else:
            result.append(l_list[l])
            l += 1
    result = result + l_list[l:]+r_list[r:]
    return result

def merge_sort(array):
    if len(array) <= 1: return array
    num = int(len(array)/2)

    # divide into
    left = merge_sort(array[:num])
    right = merge_sort(array[num:])
    return merge(left, right)
