from itertools import permutations

s, k = input().split(" ")
print("\n".join(map(lambda x: "".join(x), permutations(sorted(s), int(k)))))
