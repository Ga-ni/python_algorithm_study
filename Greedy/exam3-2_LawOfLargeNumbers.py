"""
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만든다.
단, 배역의 늑정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
입력으로 첫째 줄에 배열의 크기 N(2<=N<=1000), 숫자가 더해지는 횟수 M(1<=M<=10000), 그리고 K(1<=K<=10000)가 주어지고,
둘째 줄에 N개의 자연수가 주어진다. (다른 조건은 책 참고)
"""


n, m, k = map(int, input().split())
num_arr = list(map(int, input().split()))
result = 0
num_arr.sort() # list의 내장함수인 sort() 사용하기!

# ver1
'''
first = num_arr[n-1]
second = num_arr[n-2]

m_cnt, k_cnt = 1, 0

while m_cnt <= m:
    if k_cnt == k:
        result += second
        k_cnt = 0
    else:
        result += first
        k_cnt += 1
    m_cnt += 1'''


"""
위의 방법은 단순한 방법으로 M이 10000이하라는 조건에서는 문제가 없지만, M의 크기가 100억 이상처럼 커진다면 시간 초과가 될 수 있다.

수학적 아이디어를 이용해 효율적으로 풀어보기!
'반복되는 수열'
수열의 길이는 (k+1), 가장 큰 수가 반복되는 횟수는 (M // (k+1)) * k + (M % (k+1))
"""

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

result += first * count
result += second * (m-count)'''


print(result)

