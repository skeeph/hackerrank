print(*map(
    lambda x: "{} {}".format(x[0], x[1]),
    sorted(
        __import__('collections').Counter(input()).most_common(3),
        key=lambda c: (-c[1], c[0])
    )
), sep="\n")
