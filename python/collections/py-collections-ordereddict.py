from collections import OrderedDict

items = OrderedDict()
N = int(input())
for _ in range(N):
    line = input().rpartition(" ")
    price = int(line[2])
    name = line[0]
    items[name] = items.get(name, 0) + price

print(*[" ".join((key, str(items[key]))) for key in items], sep="\n")
