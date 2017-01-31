from collections import namedtuple

n = int(input())
Record = namedtuple("Record", " ".join(filter(lambda x: len(x) > 0, input().split(" "))))
print("{0:.2f}".format(
    sum([int(r.MARKS) for r in [
        Record(*filter(lambda x: len(x) > 0, input().split(" "))) for i in range(n)
        ]]) / n))
