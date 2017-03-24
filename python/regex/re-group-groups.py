import re
s=re.search(r"([A-Za-z0-9])\1", input())
if s is None:
    print(-1)
else:
    print(s.group()[0])