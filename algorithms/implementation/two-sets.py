from math import gcd
from functools import reduce

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
A = [int(a_temp) for a_temp in input().strip().split(' ')]
B = [int(b_temp) for b_temp in input().strip().split(' ')]


def LCM(a, b):
    return (a * b) // gcd(a, b)


lcm = reduce(LCM, A, 1)
gcd = reduce(gcd, B)

lcm_copy = lcm

count = 0
while lcm <= gcd:
    if (gcd % lcm) == 0:
        count += 1
    lcm = lcm + lcm_copy

print(count)
