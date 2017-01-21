n = int(input())
s = set(map(int, input().strip().split()))
N = int(input())
for i in range(N):
    command = input().strip().split(" ")
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))
print(sum(s))
