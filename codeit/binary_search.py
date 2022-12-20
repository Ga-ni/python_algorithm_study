def binary_search(element, some_list):
    s_idx = 0
    e_idx = len(some_list) - 1

    # while -1 < s_idx < len(some_list) and -1 < e_idx < len(some_list) :
    while s_idx <= e_idx:
        mid_idx = (s_idx + e_idx) // 2
        if some_list[mid_idx] == element:
            return mid_idx
        elif some_list[mid_idx] < element:
            s_idx = mid_idx + 1
        elif element < some_list[mid_idx]:
            e_idx = mid_idx - 1

    return None


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))