def save(n, m, s):
    return (s + m - 2) % n + 1


t = int(input().strip())
for _ in range(t):
    n, m, s = map(int, input().strip().split())
    print(save(n, m, s))
