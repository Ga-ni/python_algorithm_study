"""
N x N의 공간이 있고, 가장 왼쪽 위 좌표는 (1, 1), 가장 오른쪽 아래 좌표는 (N, N)이다.
여행가는 상하좌우로 움직일 수 있으며, 시작은 (1, 1)에서 한다.
여행가는 L, R, U, D 입력에 따라 각각 좌, 우, 상, 하로 한칸씩 이동하는데 공간을 벗어나는 입력은 무시된다.

첫 째줄에 N(1 <= N <= 100)이 주어지고,
둘 째줄에 여행가가 이동할 방향들이 주어진다. (1 <= 이동 횟수 <= 100)
결과로는 여행가가 최종적으로 도착하는 지점의 좌표를 공백으로 구분하여 출력한다.
"""

import time

# ver1

n = int(input())
path = input().split()
curX, curY = 1, 1

start1 = time.time()


for direction in path:
    if direction == "L":
        curY = curY - 1 if 0 < curY - 1 else curY
    elif direction == "R":
        curY = curY + 1 if curY + 1 <= n else curY
    elif direction == "U":
        curX = curX - 1 if 0 < curX - 1 else curX
    else:
        curX = curX + 1 if curX + 1 <= n else curX

print(curX, curY)
end1 = time.time()

print("ver1 time1 : ", end1-start1)



"""
시뮬레이션 유형!

이 문제의 연산 횟수는 이동 횟수에 비례하므로 O(N)의 시간 복잡도를 갖으며 매우 넉넉한 편이다.
"""

# ver2

n = int(input())
plans = input().split()
x, y = 1, 1

start2 = time.time()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
end2 = time.time()

print("ver2 time : ", end2-start2)
