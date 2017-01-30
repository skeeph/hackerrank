from itertools import combinations

s, k = input().split(" ")
for i in range(1,int(k)+1):
    print("\n".join(map(lambda x: "".join(x), combinations(sorted(s), i))))
