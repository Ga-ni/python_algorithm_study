"""
어떠한 수 N이 1이 될 때까지 아래 두 과정 중 하나를 반복적으로 선택하여 수행한다. 단, 2번은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
1. N에서 1을 뺀다.
2. N을 K로 나눈다.

첫 째줄에 N(2 <= N <= 100000), K(2 <= K <= 100000)이 주어지고 N은 항상 K보다 크거나 같다.
결과로는 N이 1이 될 때까지 1번 혹은 2번을 수행해야 하는 최소 갯수를 출력한다.
"""

import time



# ver1

n, k = map(int, input().split())

start1 = time.time()
cnt = 0

while n != 1:
    if n % k != 0:
        n -= 1
        cnt += 1
    else:
        first = n - 1
        second = n / k
        n = min(first, second)
        cnt += 1

print(cnt)
end1 = time.time()

print("ver1 time1 : ", end1-start1)


"""
K가 2 이상이기 때문에 최대한 많이 나누는 것이 유리하다!
빠르게 동작하도록 N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식으로 해볼 수 있다.
"""


# ver2
n, k = map(int, input().split())
start2 = time.time()
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += (n-1)
print(result)

end2 = time.time()

print("ver2 time : ", end2-start2)