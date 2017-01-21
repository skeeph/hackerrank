NA = int(input())
A = set(map(int, input().strip().split(" ")))
N = int(input())
for _ in range(N):
    command = input().strip().split(" ")
    B = set(map(int, input().strip().split(" ")))
    if command[0] == "intersection_update":
        A.intersection_update(B)
    elif command[0] == "update":
        A.update(B)
    elif command[0] == "symmetric_difference_update":
        A.symmetric_difference_update(B)
    elif command[0] == "difference_update":
        A.difference_update(B)
    elif command[0] == "difference_update":
        A.difference_update(B)

print(sum(A))
