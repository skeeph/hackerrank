x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

if (v2 >= v1 and x2 > x1) or (v1 >= v2 and x1 > x2) or (abs(x1 - x2) % abs(v1 - v2) != 0):
    print("NO")
else:
    print("YES")
