import re

s = input().strip()
print(len(re.findall(r'[A-Z]', s)) + 1)
