n, x = map(int, input().split(" "))
grades = [map(float, input().strip().split(" ")) for _ in range(x)]
print(*[sum(z)/x for z in zip(*grades)], sep="\n")