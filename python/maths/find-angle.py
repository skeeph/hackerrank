import math

AB = int(input())
BC = int(input())

theta = round(math.degrees(math.asin(AB / math.sqrt(AB ** 2 + BC ** 2))))
print('{theta:.0f}°'.format(theta=theta))
