from collections import defaultdict

d = defaultdict(list)

n, m = map(int, input().split())
for i in range(n):
    d[input()].append(i + 1)

for _ in range(m):
    s = input().rstrip()
    if s in d:
        print(' '.join(map(str, d[s])))
    else:
        print('-1')
