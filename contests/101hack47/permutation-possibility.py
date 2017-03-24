#https://www.hackerrank.com/contests/101hack47/challenges/permutation-possibility/
import sys

m = int(input().strip())
s = list(map(int, input().strip().split(' ')))
# Write Your Code Here
if len(s)==len(set(s)):
    print("YES")
else:
    print("NO")