
n, m, k = map(int, input().split())
num_arr = list(map(int, input().split()))
num_arr.sort()

# ver1
result = 0



# ver2
'''first = num_arr[n-1]
second = num_arr[n-2]
first_cnt = (m // (k+1)) * k + m % (k+1)
result = (first * first_cnt) + (second * (m // (k+1)))'''


# ver3
'''first = num_arr[n-1]
second = num_arr[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += first * count
result += second * (m-count)'''


print(result)

