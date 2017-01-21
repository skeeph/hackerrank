A = set(map(int, input().strip().split(" ")))
n = int(input())
superset = True
for _ in range(n):
    B = set(map(int, input().strip().split(" ")))
    if len(A.difference(B)) == 0 or len(B.difference(A)) > 0:
        superset = False
        break

print(superset)
