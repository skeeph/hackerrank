cube = lambda x: x ** 3


def fibonacci(n):
    fibs = []
    for i in range(n):
        fibs.append(i if i < 2 else fibs[i - 2] + fibs[i - 1])
    return fibs


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
