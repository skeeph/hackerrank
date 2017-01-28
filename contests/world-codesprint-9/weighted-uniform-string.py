from string import ascii_lowercase

weights = dict(zip(ascii_lowercase, range(1, len(ascii_lowercase) + 1)))


def checkSum(s: str, w: int) -> bool:
    for k in weights:
        wk = weights[k]
        if w % wk == 0:
            z = k * (w // wk)
            if z in s and len(z) > 0:
                return True
    return False


if __name__ == '__main__':
    S = input()
    for _ in range(int(input())):
        x = int(input())
        if checkSum(S, x):
            print("Yes")
        else:
            print("No")
