def reverse(num):
    return int(str(num)[::-1])


def beautiful(num, k):
    return abs(num - reverse(num)) % k == 0


i, j, k = map(int, input().strip().split(" "))
print(len(list(filter(lambda x: beautiful(x, k), range(i, j + 1)))))
