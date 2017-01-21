T = int(input())
for _ in range(T):
    na = int(input())
    A = set(map(int, input().strip().split(" ")))
    nb = int(input())
    B = set(map(int, input().strip().split(" ")))
    if len(A.difference(B)) == 0:
        print(True)
    else:
        print(False)
