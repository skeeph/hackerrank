n, k = map(int, input().split())
rq, cq = map(int, input().split())
obstacles = [tuple(map(int, input().split())) for i in range(k)]
ro = []
co = []

for i in obstacles:
    if i[0] == rq:
        co.append(i[1])
    if i[1] == cq:
        ro.append(i[0])

leftOb = list(filter(lambda x: x < cq, co)) + [0]
rightOb = list(filter(lambda x: x > cq, co)) + [n + 1]
topObs = list(filter(lambda x: x > rq, ro)) + [n + 1]
bottomObs = list(filter(lambda x: x < rq, ro)) + [0]

left = abs(max(leftOb) - cq) - 1
right = min(rightOb) - cq - 1
bottom = abs(max(bottomObs) - rq) - 1
top = min(topObs) - rq - 1
print(left, top, right, bottom)

ld = list(filter(lambda x: x[0] < rq and x[1] < cq and cq - x[0] == rq - x[1], obstacles))
lt = list(filter(lambda x: x[0] > rq and x[1] < cq and cq - x[0] == rq + x[1], obstacles))
rt = list(filter(lambda x: x[0] > rq and x[1] > cq and cq + x[0] == rq + x[1], obstacles))
rd = list(filter(lambda x: x[0] < rq and x[1] > cq and cq - x[0] == rq + x[1], obstacles))

