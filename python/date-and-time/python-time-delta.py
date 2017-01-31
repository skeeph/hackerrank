from dateutil.parser import parse

for _ in range(int(input())):
    s = parse(input())
    t = parse(input())
    print(abs(int((s - t).total_seconds())))
