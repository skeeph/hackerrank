from collections import Counter

x = int(input())
sz = Counter(map(int, input().split(" ")))
n = int(input())
money = 0
for _ in range(n):
    s, price = map(int, input().split())
    if sz[s] > 0:
        money = money + price
        sz[s] -= 1

print(money)