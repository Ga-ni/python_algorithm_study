"""
# 예제 3-1
거스름돈 n을 무한한 갯수의 동전 종류 500원, 100원, 50원, 10원을 가지고 줄때,
최소한의 동전 갯수를 구해라.
"""


n = int(input())
count = 0
coin_list = [500, 100, 50, 10]

for coin in coin_list:
    count += n // coin
    n %= coin

print(count)