

def solution():
    n, k = map(int, input().split())
    input_list = list(map(int, input().split()))

    sorted_list = sorted(input_list)
    tmp = sorted_list[-k:]

    unsorted = [a for a in input_list if a not in tmp]
    # print(unsorted + tmp)

    for i in unsorted + tmp:
        print(i, end=" ")


    # for i in range(n - 1, n - 1 - k, -1):
    #     for j in range(0, i):
    #         if input_list[j] > input_list[j + 1]:
    #             tmp = input_list[j]
    #             input_list[j] = input_list[j + 1]
    #             input_list[j + 1] = tmp


    # print(input_list)



if __name__ == '__main__':
    solution()

# 10 3
# 10 9 8 7 6 5 4 3 2 1