for i in range(1, int(input()) + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    # (10 ** i - 1) ** 2 // 81
    print("".join(map(str, list(range(1, i)) + list(range(i, 0, -1)))))
