from itertools import groupby
print(*[(len(list(i[1])), int(i[0])) for i in groupby(input())])