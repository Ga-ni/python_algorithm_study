"""
아래 룰을 지키며 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
1. 숫자가 쓰인 카드틀이 N행 x M열 형태로 놓여있다.
2. 먼저 뽑으려는 카드가 있는 행을 선택한다.
3. 선택된 행에 있는 카드들 중 가장 숫자가 작은 카드를 뽑아야 한다.

N과 M이 첫 줄에 주어지고, 다음줄부터 N개의 줄에 걸쳐 카드 숫자가 주어진다.
(1 <= N,M <= 100), 카드의 숫자는 1이상 10000 이하의 자연수이다.
"""

# ver1
'''n, m = map(int, input().split())
mins = []

for row in range(n):
    tmp = map(int, input().split())
    mins.append(min(tmp))

max = mins[0]
for num in mins:
    if max < mins[num]:
        max = mins[num]

print(max)'''


"""
min, max 함수에 list 자료형이 들어가는 것이 가능하다.
"""


# ver2
'''n, m = map(int, input().split())
mins = []

for row in range(n):
    mins.append(min(list(map(int, input().split()))))

print(max(mins))'''


# ver3
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_val = min(data)
    result = max(result, min_val)

print(result)