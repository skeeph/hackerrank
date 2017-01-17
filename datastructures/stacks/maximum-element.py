class Stack:
    def __init__(self):
        self.s = list()
        self._max = list()

    def push(self, x):
        if len(self._max) == 0:
            self._max.append(x)
        elif x > self._max[-1]:
            self._max.append(x)
        self.s.append(x)

    def pop(self):
        if self.s[-1] == self._max[-1]:
            self._max.pop(-1)
        return self.s.pop(-1)

    def max(self):
        if self._max:
            return self._max[-1]
        else:
            return 0


if __name__ == '__main__':
    n = int(input())
    s = Stack()
    for _ in range(n):
        q = list(map(int, input().strip().split(" ")))
        if q[0] == 1:
            s.push(q[1])
        elif q[0] == 2:
            s.pop()
        elif q[0] == 3:
            print(s.max())