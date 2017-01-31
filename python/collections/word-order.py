from collections import Counter

c = Counter([input().strip() for i in range(int(input()))])
print(len(c))
print(" ".join(map(str,c.values())))
