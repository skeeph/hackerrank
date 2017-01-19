n = int(input().strip())
liked = [5 // 2]
for i in range(1, n):
    liked.append(
        (liked[i - 1] * 3) // 2
    )

print(sum(liked))
