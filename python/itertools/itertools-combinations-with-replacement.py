from itertools import combinations_with_replacement

s, k = input().split(" ")
print("\n".join(map(lambda x: "".join(x), combinations_with_replacement(sorted(s), int(k)))))
