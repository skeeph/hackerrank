n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

print(sum([c.count(ci) // 2 for ci in set(c)]))
