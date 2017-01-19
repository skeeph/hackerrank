(n, m) = map(int, input().split())

array = list(map(int, input().split()))
assert len(array) == n

A = set(map(int, input().split()))
assert len(A) == m

B = set(map(int, input().split()))
assert len(B) == m

happiness = 0

for i in array:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1

print(happiness)