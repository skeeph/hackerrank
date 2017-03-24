import re

pattern = re.compile(r"^[+-]?\d*\.\d*$")
n = int(input())
for i in range(n):
    if pattern.match(input()):
        print(True)
    else:
        print(False)