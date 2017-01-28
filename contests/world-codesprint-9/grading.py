def _round(grade: int) -> int:
    nextFive = grade - grade % 5 + 5
    if abs(grade - nextFive) < 3 and grade >= 38:
        grade = nextFive
    return grade


if __name__ == '__main__':
    n = int(input())
    grades = []
    for _ in range(n):
        grades.append(int(input()))
    print("\n".join(map(str, map(_round, grades))))
